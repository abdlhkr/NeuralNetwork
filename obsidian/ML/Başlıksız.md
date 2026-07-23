# Çok Şubeli Restoran Sipariş ve QR Masa Yönetim Platformu

## 1. Görevin

Aşağıda ayrıntıları verilen , çok şubeli restoran yönetimi ve müşteri sipariş platformu için:

1. Ölçeklenebilir sistem mimarisi tasarla.
    
2. Sistemi mikroservis mimarisine uygun şekilde böl.
    
3. Servislerin görevlerini ve sınırlarını belirle.
    
4. Veritabanı modellerini tasarla.
    
5. Servisler arası senkron ve asenkron iletişimi belirle.
    
6. Gerçek zamanlı sipariş akışını tasarla.
    
7. API endpoint taslaklarını oluştur.
    
8. Event isimlerini ve event payload yapılarını belirle.
    
9. Yetkilendirme ve rol modelini tasarla.
    
10. Yüksek trafik, hata toleransı, log sistemi,güvenlik ve veri tutarlılığı için çözüm öner.
    
11. MVP ve sonraki sürümler için aşamalı geliştirme planı oluştur.
    
12. Monorepo veya polyrepo seçimini gerekçelendir.
    
13. Teknoloji yığınını gerekçeleriyle öner.
    
14. Kritik kullanıcı akışları için sequence diagramları Mermaid formatında hazırla.
    
15. Geliştirmeye başlanabilecek klasör yapısı ve başlangıç yol haritası oluştur.
    

Sadece genel tavsiye verme. Gerçek bir yazılım projesi geliştirilecekmiş gibi teknik kararlar, veri modelleri, servis sınırları, eventler, hata senaryoları ve ölçeklendirme stratejileri sun.

---

# 2. Ürün Tanımı

Sistem, restoran, kafe ve benzeri yiyecek-içecek işletmelerinin kayıt olabildiği, şube açabildiği, menülerini yönetebildiği ve müşterilerin masalardaki QR kodlar üzerinden sipariş verebildiği bir platform olacaktır.

Platform üç ana kullanıcı grubuna hizmet edecektir:

- İşletme sahipleri
    
- Şube personelleri
    
- Restoran müşterileri
    

İlk aşamada:

- İşletme yönetim paneli web uygulaması olacaktır.
    
- Şube mutfak ve kasa ekranları web uygulaması olacaktır.
    
- Müşteri tarafı responsive web uygulaması olacaktır.
    
- Daha sonra iOS ve Android mobil uygulamaları geliştirilecektir.
    
- Ödeme sistemi sonraki aşamada eklenecektir.
    
- Bildirim ve analitik ekranları sonraki aşamada eklenecektir.
    

Backend, web ve mobil uygulamalar tarafından ortak kullanılabilecek şekilde API-first tasarlanmalıdır.

---

# 3. Temel Mimari Hedefler

Sistem aşağıdaki özelliklere sahip olmalıdır:

- Multi-tenant yapı
    
- Mikroservis mimarisi
    
- Event-driven ve asenkron işlem desteği
    
- Gerçek zamanlı sipariş güncellemeleri
    
- Yüksek trafik altında yatay ölçeklenebilme
    
- Bir işletmenin verisinin diğer işletmelerden kesin olarak ayrılması
    
- Aynı şube hesabının birden fazla cihazda kullanılabilmesi
    
- Web ve mobil uygulamalar için ortak backend
    
- Eventual consistency gerektiren yerlerde kontrollü veri tutarlılığı
    
- Tekrarlanan isteklerde idempotency
    
- Hata durumlarında retry ve dead-letter queue desteği
    
- Gözlemlenebilirlik, loglama, tracing ve metric desteği
    
- KVKK ve temel güvenlik standartlarına uygunluk
    
- Ödeme sistemi sonradan eklenebilecek genişletilebilir tasarım
    

Servislerin gereksiz yere birbirine bağımlı olduğu “dağıtık monolit” yapısından kaçınılmalıdır.

Her mikroservis kendi iş alanına ve mümkünse kendi veritabanına sahip olmalıdır.

direk mikroservis

---

# 4. Kullanıcı ve Hesap Yapısı

## 4.1 İşletme hesabı

Bir işletme aşağıdaki yöntemlerle kayıt olabilir:

- E-posta ve şifre
    
- Google ile giriş
    
 kayıt anında telefon numarası ad soyad cinsiyet gibi temel bilgilerde istenmelidir
E-posta ile kayıt olan kullanıcının e-posta adresi doğrulanmalıdır.

İşletme hesabı oluşturulduğunda:

- İşletme profili oluşturulur.
    
- İşletmeye ait varsayılan menü oluşturulur.
    
- İşletme sahibi OWNER rolüne sahip olur.
    
- İşletme daha sonra birden fazla şube açabilir.
    

İşletme hesabı için desteklenmesi gereken işlemler:

- Kayıt olma
    
- E-posta doğrulama
    
- Giriş yapma
    
- Google ile giriş
    
- Şifremi unuttum
    
- Şifre sıfırlama
    
- E-posta adresi değiştirme
    
- Yeni e-posta adresini doğrulama
    
- Aktif oturumları görüntüleme
    
- Belirli cihazlardaki oturumları kapatma
    
- Tüm cihazlardan çıkış yapma
son üçü çokta gerekli olmayabilir sen karar ver buna 

## 4.2 Şube hesabı

Her şube bir e-posta adresiyle ilişkilendirilir.

Şube oluşturulurken:

- İşletme sahibi şube için e-posta adresi girer.
    
- Şube e-posta adresine davet veya doğrulama bağlantısı gönderilir.
    
- E-posta sahibi adresi doğrular.
    
- Şube hesabı için şifre belirler veya Google ile giriş yapar.
    
- Aynı şube hesabı aynı anda birden fazla cihazda açılabilir.
    
- İşletme sahibi daha sonra şube e-posta adresini değiştirebilir.
    
- Yeni e-posta adresi doğrulanmadan değişiklik tamamlanmamalıdır.
    
- Şube hesabı şifremi unuttum işlemini kullanabilmelidir.
    

Şube hesabında giriş yaptıktan sonra en az iki çalışma alanı bulunacaktır:

- Mutfak ekranı
    
- Kasa ekranı
sonrası için garsonlar

Ancak güvenlik açısından tek bir paylaşılan şube hesabının mı kullanılacağı, yoksa çalışanların ayrı hesaplarla şubeye üye yapılacağı mı daha doğru olacağını değerlendir.

Tercih edilen uzun vadeli çözüm:

- Her çalışanın kendi kullanıcı hesabı bulunması
    
- Kullanıcının şubeye bir rol ile atanması
    
- KITCHEN, CASHIER, BRANCH_MANAGER gibi roller
    
- Ortak mutfak ekranları için güvenli cihaz oturumu veya kiosk modu
    
bu şu anlık çokta gerekli değil önemli olan mutfak kasa ve ilerisi için garson bu rollere direk mail ile kaydolanibilir 


## 4.3 Müşteri hesabı

Müşteri uygulaması aşağıdaki giriş yöntemlerini desteklemelidir:

- E-posta ve şifre
    
- Google ile giriş
    
- İleride Apple ile giriş eklenebilmesi şimdilik atla 
    

Müşteri hesabı olmadan QR kod üzerinden geçici misafir oturumu açılıp açılamayacağını değerlendir.
bunu yapma giriş yapmayı zaten google ile desteklendiği için direk mail adresiyle hesap oluşturup hızlıca kaydolabilisin

Tercih edilen kullanıcı deneyimi:

- Kullanıcı QR kodu okuduğunda sipariş vermeden önce hesap oluşturmak zorunda kalmalı ama bu işlem olabildiğince kolay olmalı 


---

# 5. Yetki Modeli

Önerilen rol yapısı:

## İşletme seviyesinde

- BUSINESS_OWNER
    
- BUSINESS_ADMIN
    
- BUSINESS_VIEWER
    

## Şube seviyesinde

- BRANCH_MANAGER
    
- CASHIER
    
- KITCHEN
    
- STAFF
    

## Platform seviyesinde platform seviyesinden kastın ne bana  çok mantıksız geldi bu olmayabilir 

- PLATFORM_ADMIN
    
- SUPPORT_AGENT
    

## Müşteri seviyesinde

- CUSTOMER

Rol ve izin sistemi yalnızca sabit rol adına bağlı bırakılmamalıdır. Permission tabanlı bir yapı da değerlendirilmelidir.

Örnek izinler:

- business.update
    
- branch.create
    
- branch.update
    
- branch.delete
    
- branch.email.change
    
- menu.read
    
- menu.manage
    
- stock.manage
    
- table.manage
    
- order.create
    
- order.cancel
    
- order.cancel.after_window
    
- kitchen.order.update
    
- cashier.order.view
    
- cashier.order.cancel
    
- analytics.view
    

Her istekte aşağıdakiler doğrulanmalıdır:

- Kullanıcı kimliği
    
- İşletme üyeliği
    
- Şube üyeliği
    
- Rol ve izin
    
- Kaynağın ilgili işletme veya şubeye ait olması
    

Tenant izolasyonu sadece frontend veya request parametresine güvenerek yapılmamalıdır.

---

# 6. İşletme ve Şube Yönetimi

## 6.1 İşletme bilgileri

İşletme için en az aşağıdaki alanlar bulunmalıdır:

- ID
    
- İşletme adı
    
- Logo (resim)
    
- Kapak resmi (yatay resim)
    
- Telefon
    
- E-posta
    
- Oluşturulma tarihi
    
- Durum
    
- Varsayılan para birimi (şu anlık default tl olsun) 
    
- Varsayılan dil (varsayılan direk türkçe) 
    
- Zaman dilimi (varsayılan yine tr) 
    

İlk ülke Türkiye olacaktır.

Varsayılan para birimi:

- TRY
    

Varsayılan zaman dilimi:

- Europe/Istanbul
    

## 6.2 Şube bilgileri

Her şube aşağıdaki alanlara sahip olmalıdır:

- ID
    
- businessId
    
- Şube adı
    
- Şube açıklaması
    
- Şube e-posta adresi
    
- Şube e-posta doğrulama durumu
    
- Telefon
    
- Ülke (default türkiye bundan sonrası api ile liste şeklinde çeekilerek dropdown menü olarak listelenmelidir) 
    
- İl
    
- İlçe
    
- Mahalle
    
- Sokak veya cadde
    
- Apartman veya bina numarası
    
- Daire numarası
    
- Posta kodu
    
- Google Maps bağlantısı
    
- Çalışma saatleri
    
- Şube durumu
    
- Sipariş alıyor mu?
    
- Oluşturulma tarihi
    
- Güncellenme tarihi
    

Zorunlu adres alanları:

- İl
    
- İlçe
    
- Mahalle
    
- Sokak veya cadde
    
- Bina/apartman numarası
    
- Daire numarası
 google maps linki https://maps.app.goo.gl/SPHqtmAKzQJRDtka7 mesela bu formatta yani

Daire numarası bulunmayan müstakil işletmeler olabileceği için ürün gereksinimini sorgula. Daha doğru çözüm olarak:

- addressDetails veya ek adres açıklaması zorunlu
    
- apartmentNumber veya suiteNumber opsiyonel
    

yapısını değerlendir.

## 6.3 Türkiye adres seçimi

İl, ilçe ve mahalle alanları birbirine bağlı seçim kutuları olacaktır.

Akış:

1. Ülke Türkiye şimdilik sabit 
    
2. İl listesi alınır.
    
3. İl seçildiğinde ilçeler alınır.
    
4. İlçe seçildiğinde mahalleler alınır.
    
5. Sokak, bina numarası ve diğer ayrıntılar kullanıcı tarafından girilir.
    

Harici adres API'si kullanılacak burda 

Şu alternatifleri karşılaştır:

- Harici Türkiye adres API'si kullanmak
    
- İl, ilçe ve mahalle verilerini sistem veritabanına aktarmak
    
- Harici API'den periyodik senkronizasyon yapmak
    
- Google Places veya başka bir adres doğrulama servisi kullanmak
    

Harici servis geçici olarak erişilemez olduğunda işletme oluşturma işlemi tamamen bozulmamalıdır.

Adres kayıtlarında yalnızca il, ilçe ve mahalle adları değil, mümkünse sabit kimlikleri de saklanmalıdır.

---

# 7. Görsel Depolama

Menü ürünleri, işletme logoları ve şube görselleri uygulama sunucusunun yerel diskinde tutulmayacaktır.

Aşağıdaki seçenekleri değerlendir:

- Amazon S3 ve CDN
    
- Cloudflare R2 ve CDN
    
- Google Cloud Storage
    
- Azure Blob Storage
    
- Cloudinary
    
- Supabase Storage
    
- MinIO tabanlı S3 uyumlu özel depolama
    

Önerilen yaklaşım:

- Üretim ortamında S3 uyumlu object storage
    
- Görsellerin CDN üzerinden sunulması
    
- Backend'in presigned upload URL üretmesi
    
- Frontend'in görseli doğrudan object storage'a yüklemesi
    
- Backend üzerinden büyük dosya aktarılmaması
    
- Veritabanında sadece object key, URL ve metadata saklanması
    

Görseller için:

- Dosya türü doğrulama
    
- MIME type kontrolü
    
- Boyut sınırı
    
- Zararlı dosya kontrolü
    
- EXIF metadata temizliği
    
- Thumbnail üretimi
    
- WebP veya AVIF dönüşümü
    
- Farklı çözünürlükler
    
- Silinen görseller için garbage collection
    
- Yetkisiz özel dosya erişimine karşı signed URL
    

tasarlanmalıdır.

Başlangıç için Cloudinary'nin operasyon kolaylığı ile Cloudflare R2 veya S3'ün uzun vadeli esnekliği karşılaştırılmalıdır.

---

# 8. Varsayılan Menü Sistemi

İşletme oluşturulduğunda otomatik bir varsayılan menü şablonu oluşturulacaktır.

Örnek kategoriler:

- Kahvaltı
    
- Öğle yemekleri
    
- Ana yemekler
    
- Ara sıcaklar
    
- Tatlılar
    
- Kahveler
    
- Sıcak içecekler
    
- Soğuk içecekler
    

Bu kategoriler sistem şablonundan kopyalanmalı, ancak işletme tarafından değiştirilebilmelidir.

İşletme:

- Yeni kategori ekleyebilmeli
    
- Kategori adını değiştirebilmeli
    
- Kategoriyi silebilmeli veya pasife alabilmeli
    
- Kategori sırasını değiştirebilmeli
    
- Ürün ekleyebilmeli
    
- Ürün düzenleyebilmeli
    
- Ürün silebilmeli veya arşivleyebilmeli
    

## 8.1 Menü ürünü

Her menü ürünü için en az aşağıdaki alanlar bulunmalıdır:

- ID
    
- businessId
    
- Kategori ID
    
- Ürün adı
    
- Ürün görseli
    
- Ana fiyat
    
- Para birimi
    
- Hazırlanma süresi
    
- Aktif mi?
    
- Menüde görünüyor mu?
    
- Sıralama değeri
    
- İçerik seçenekleri
    
- Oluşturulma tarihi
    
- Güncellenme tarihi
## 8.2 İçerik ve ürün özelleştirmeleri

Sistemde varsayılan içerik seçenekleri bulunacaktır.

Örnekler:

- Patates
    
- Turşu
    
- Soğan
    
- Domates
    
- Marul
    
- Ketçap
    
- Mayonez
    
- Peynir
    

Ancak bu yapı yalnızca “içindekiler” şeklinde modellenmemelidir. İki farklı kavram ayrılmalıdır:

### Bilgilendirici içerikler

Ürünün normal içeriğini gösterir.

Örnek:

- Dana eti
    
- Ekmek
    
- Marul
    
- Domates
    

### Seçilebilir özelleştirmeler

Müşterinin seçim yapmasını sağlar.

Örnek:

- Turşu olsun veya olmasın
    
- Patates boyutu
    
- Ekstra peynir
    
- Pişirme derecesi
    
- Sos seçimi
    

Önerilen yapı:

- ModifierGroup
    
- ModifierOption
    

ModifierGroup alanları:

- ID
    
- Ad
    
- Zorunlu mu?
    
- Minimum seçim
    
- Maksimum seçim
    
- Tek seçim veya çoklu seçim
    
- Sıralama
    
- Aktiflik
    

ModifierOption alanları:

- ID
    
- Ad
    
- Ek fiyat
    
- Varsayılan olarak seçili mi?
    
- Seçilebilir mi?
    
- Stokta mı?
    
- Sıralama
    

Örnek:

“Yan ürün seçimi” grubu:

- Minimum seçim: 1
    
- Maksimum seçim: 1
    
- Patates: +0 TL
    
- Soğan halkası: +25 TL
    
- Salata: +15 TL
    

Sipariş oluşturulduğunda ürün adı, ürün fiyatı ve seçilen seçenekler snapshot olarak siparişe kaydedilmelidir. Daha sonra menü fiyatı değişse bile geçmiş sipariş değişmemelidir.

---

# 9. İşletme Menüsü ve Şube Menüsü

Menü için kalıtım veya override sistemi tasarlanmalıdır.

## İşletme ana menüsü

İşletmenin merkezi menüsüdür.

## Şube menüsü

Her şube işletmenin ana menüsünü varsayılan olarak kullanır fakat:

- Bazı ürünleri şubede gizleyebilir.
    
- Bazı ürünleri şubede aktif veya pasif yapabilir.
    
- Şubeye özel ürün ekleyebilir.
    
- Şubeye özel fiyat belirleyebilir.
    
- Şubeye özel içerik seçeneği belirleyebilir.
    
- Ürünü geçici olarak stokta yok olarak işaretleyebilir.
    
- Kategori sırasını değiştirebilir.
    
- Çalışma saatine göre ürün kullanılabilirliğini değiştirebilir.
    

Verinin her şube için tamamen kopyalanması ile merkezi menü artı şube override modeli karşılaştırılmalıdır.

Tercih edilen yaklaşım:

- Merkezi ürün tanımı
    
- BranchMenuItem veya BranchProductOverride tablosu
    
- Şubeye özel override alanları
    
- Sipariş sırasında çözülmüş ürün verisi
    

Şube override örnek alanları:

- branchId
    
- productId
    
- priceOverride
    
- isVisible
    
- isAvailable
    
- stockStatus
    
- availabilitySchedule
    
- preparationTimeOverride
    

İşletme ana menüsünde yapılan değişikliklerin şube override kayıtlarını nasıl etkileyeceği açıkça tanımlanmalıdır.

---

# 10. Anlık Stok Durumu

Şube personeli bir ürünü veya ürün seçeneğini:

- Stokta
    
- Geçici olarak tükendi

durumlarından birine getirebilmelidir.

Bir ürün tükendiğinde:

- Müşteri ekranından gerçek zamanlı olarak kaldırılmalı veya “tükendi” gösterilmelidir.
    
- Sepete daha önce eklenmişse sipariş gönderme sırasında yeniden doğrulanmalıdır. (burda sıkıntı yok kasadan siler bu işleve gerek yok )
    
- Mutfak ve kasa ekranları güncellenmelidir.
    
- Cache invalidate edilmelidir.
    

Yalnızca frontend'deki stok bilgisine güvenilmemelidir.

Sipariş oluşturulurken backend ürünün hâlâ sipariş verilebilir olduğunu kontrol etmelidir.

İlk aşamada adet bazlı envanter takibi zorunlu değildir. “Var/yok” tipi stok durumu yeterlidir.

Ancak mimari gelecekte şu özellikleri destekleyebilmelidir:

- Adet bazlı ürün stoğu
    
- Hammadde stoğu
    
- Reçete bazlı stok düşümü
    
- Kritik stok bildirimi
    
- Şubeler arası stok farkı
    

---

# 11. Masa ve Alan Yönetimi

Her şube kendi masa veya servis noktalarını oluşturabilir.

Masa kavramı yalnızca fiziksel masa numarası olarak sınırlandırılmamalıdır.

Kullanıcı aşağıdaki gibi isimler verebilir: sistem şu şekilde şube oluşturmak istediği masa sayısını ve bu masalara vermke istediği adı giricek buna bağlı olarak mesela ad balkon verdi balkon 1 balkon 2 ... masalar ve qr lar oluşturulacak

Masa için zorunlu bir ad formatı bulunmayacaktır.

Her masa için:

- ID
    
- branchId
    
- Alan/bölge ID
    
- Kapasite
    
- Aktiflik
    
- Kalıcı public QR identifier
    
- Oluşturulma tarihi
    
- Güncellenme tarihi
    

bulunmalıdır.

## 11.1 Alanlar

Şube isteğe bağlı alanlar oluşturabilir:

- İç mekan
    
- Dış mekan
    
- Balkon
    
- Teras
    
- Bahçe
    
- Üst kat
    

Alan kullanımı zorunlu olmamalıdır.

## 11.2 QR kod

Her masanın kendine ait QR kodu olacaktır.

Temel gereksinim:

- QR kodun public identifier değeri normal şartlarda değişmeyecek.
    
- QR yeniden yazdırıldığında aynı masaya yönlendirecek.
    
- Dahili database ID doğrudan QR içine yazılmayacak.
    
- Tahmin edilebilir artan ID kullanılmayacak.
    
- QR içinde güvenli ve rastgele bir token veya slug bulunacak.
    

Örnek:

`https://app.example.com/t/{publicTableToken}`

QR kod değişmez olsa da güvenlik için sistemde şu özellik bulunmalıdır:

- İşletme sahibi QR kodu manuel olarak yenileyebilmeli.
    
- Eski QR token iptal edilebilmeli.
    
- Kötüye kullanım tespit edilirse token rotate edilebilmeli.

QR kod tek başına süresiz sipariş yetkisi vermemelidir.

Uzaktan QR fotoğrafını alan bir kişinin sipariş vermesini azaltmak için şu seçenekleri değerlendir:

- Restoran konumuna yakınlık kontrolü max 300 m gibi
    
- Kısa ömürlü masa erişim tokenı
    
- Riskli siparişlerde kasa onayı adet sayısına bağlı düşünülebilir 100 tane girmesin sipariş


Konum kontrolünün tek başına kesin güvenlik sağlamadığı belirtilmelidir.

---

# 12. Masa Oturumu

Müşteri QR kodu okuttuğunda doğrudan kalıcı masaya değil, aktif bir TableSession kaydına bağlanmalıdır.

TableSession alanları:

- ID
    
- branchId
    
- tableId
    
- status
    
- ownerParticipantId
    
- openedAt
    
- closedAt
    
- lastActivityAt
    
- sessionCode
    
- version
    
- totalAmountSnapshot
    
- currency
    

Durumlar:

- OPEN
    
- WAITING_FOR_OWNER
    
- ACTIVE
    
- PAYMENT_REQUESTED
    
- CLOSED
    
- EXPIRED
    
- CANCELLED
    

## 12.1 İlk müşteri

QR kodu okutup aktif masa oturumuna ilk katılan müşteri masa oturumunun sahibi olur.

Bu kullanıcı:

- Masa sahibi
    
- Session owner
    
- Oturum yöneticisi
    

olarak kabul edilir.

## 12.2 Sonraki müşteriler

Aynı QR kodu okutan diğer müşteriler otomatik olarak masaya dahil edilmez.

Akış:

1. Yeni müşteri QR kodu okutur.
    
2. Sistemde açık masa oturumu bulunur.
    
3. Join request oluşturulur.
    
4. Masa sahibine gerçek zamanlı katılım isteği gönderilir.
    
5. Masa sahibi isteği kabul veya reddeder.
    
6. Kabul edilirse müşteri masa oturumuna katılır.
    
7. Reddedilirse sipariş verme yetkisi verilmez.
    

Katılım isteği belirli süre sonra sona ermelidir.

Örnek süre:

- 5 dakika

## 12.3 Masa sahibi ayrılırsa

Aşağıdaki durumları tasarla:

- Masa sahibi oturumdan ayrılırsa yeni sahip seçilmesi burda direk rastgele biri seçilebilir sorun değil bu masada aktif oturumu olan 
    
- Sahip internet bağlantısını kaybederse
    
- Sahip telefonu kapanırsa
    
- Sahip join request'i görmezse
    
- Masada yalnızca bir kişi kalırsa
    
- Tüm müşteriler ayrılırsa
    
- Masa uzun süre işlem görmezse
    
- Şube personeli oturumu kapatırsa
    

Önerilen çözüm: bu kısım tamane gereksiz uygulama karmaşası atla burayı

- Masa sahibinin bağlantısı koptuğunda sahiplik hemen kaldırılmamalı.
    
- Belirli grace period uygulanmalı.
    
- Masa sahibi manuel olarak başka katılımcıya sahipliği devredebilmeli.
    
- Kasa personeli masa oturumunu yönetebilmeli.
    
- Son aktiviteye göre otomatik expiration uygulanmalı.

    

---

# 13. Sepet Sistemi

Her müşterinin aynı masa oturumunda kendi sepeti bulunmalıdır.

Sepet aşağıdaki bilgileri içermelidir:

- Müşteri veya guest session
    
- TableSession
    
- Ürün
    
- Adet
    
- Seçilen modifier seçenekleri
    
- Not
    
- Hesaplanan fiyat
    
- Güncellenme zamanı
    

Sepet kişisel olmalıdır.

Diğer masa katılımcılarının sepetleri sipariş verilmeden önce varsayılan olarak görünmemelidir.

Sipariş gönderildikten sonra masanın ortak sipariş geçmişinde gösterilebilir.

Sepetteki fiyat kesin fiyat değildir. Sipariş oluşturulurken backend tarafından tekrar hesaplanmalıdır.

Backend şunları yeniden kontrol etmelidir:

- Ürün aktif mi?
    
- Ürün şubede bulunuyor mu?
    
- Ürün stokta mı?
    
- Modifier seçenekleri geçerli mi?
    
- Minimum ve maksimum seçim kuralları sağlanıyor mu?
    
- Fiyat değişmiş mi?
    
- Şube sipariş kabul ediyor mu?
    
- Masa oturumu aktif mi?
    
- Kullanıcı masa oturumunun katılımcısı mı?
    

---

# 14. Sipariş Oluşturma ve 10 Saniyelik İptal Süresi

Müşteri sipariş verdiğinde sipariş oluşturulur.

Ancak müşteri siparişi yalnızca ilk 10 saniye içinde doğrudan iptal edebilir.

10 saniye geçtikten sonra:

- Müşteri doğrudan iptal edemez.
    
- Müşteri kasadan veya personelden iptal talep etmek zorundadır.
    
- Yetkili kasa personeli sipariş kalemini iptal edebilir.
    

## 14.1 Sipariş durumları

Önerilen Order durumları:

- DRAFT
    
- PENDING_CONFIRMATION
    
- CONFIRMED
    
- IN_PREPARATION
    
- READY
    
- SERVED

bundan sonraki kısımlar masa geneli hesap olarak olucak kullanıcı özelinde değil 
- PAYMENT_REQUESTED
    
- COMPLETED
    
- PARTIALLY_CANCELLED
    
- CANCELLED
    
- REJECTED
    

OrderItem durumları:

- PENDING_CONFIRMATION
    
- CONFIRMED
    
- IN_PREPARATION
    
- READY
    
- SERVED
    
- CANCELLED
    
- REJECTED
    

## 14.2 İlk 10 saniye

Sipariş verildiğinde:

1. Sipariş veritabanına yazılır.
    
2. Durumu PENDING_CONFIRMATION olur.
    
3. cancelUntil alanı sunucu zamanı ile hesaplanır.
    
4. Müşteriye 10 saniyelik iptal hakkı gösterilir.
    
5. 10 saniye içinde müşteri iptal ederse sipariş CANCELLED olur.
    
6. Süre dolarsa sipariş CONFIRMED olur.
    
7. CONFIRMED olduktan sonra mutfak ekranına gönderilir.
    
8. Kasa toplamı güncellenir.
    
9. Masa oturumundaki diğer kullanıcılar bilgilendirilir.
    

10 saniyelik işlem uygulama sunucusunda `setTimeout` kullanılarak yapılmamalıdır.

Sunucu yeniden başlasa bile işlem kaybolmamalıdır.

Şu çözümleri değerlendir:

- Delayed message queue
    
- Redis tabanlı durable job queue
    
- RabbitMQ delayed message
    
- PostgreSQL tabanlı job scheduler
    
- Transactional outbox ve scheduler kombinasyonu
    

MVP için güvenilir ve operasyonel olarak makul bir çözüm öner.

## 14.3 Zaman güvenliği

10 saniyelik süre frontend saatine göre değil, backend saatine göre hesaplanmalıdır.

Response içinde:

- serverTime
    
- cancelUntil
    

alanları dönmelidir.

Frontend sadece görsel geri sayım göstermelidir.

Nihai iptal yetkisini backend belirlemelidir.

## 14.4 Yarış koşulları

Aşağıdaki yarış koşullarını çöz:

- Müşteri tam 10. kullanıcıya on de ilk 15 saniye kabul et hiç gerek yok karmaşaya saniyede iptal gönderirse
    
- Worker siparişi onaylarken iptal isteği gelirse worker 
    
- Aynı iptal isteği iki kere gönderilirse
    
- İki farklı cihaz aynı siparişi iptal etmeye çalışırsa
    
- Mesaj kuyruğu aynı eventi birden fazla gönderirse
    

Optimistic locking, version field, atomic update ve idempotency key kullanımını değerlendir.

---

# 15. Mutfak Ekranı

Mutfak ekranında yalnızca CONFIRMED durumuna geçmiş siparişler görüntülenmelidir.

Mutfak ekranı için:

- Yeni siparişler gerçek zamanlı gelmeli
    
- Sipariş sesi opsiyonel olmalı
    
- Masa adı görünmeli
    
- Sipariş zamanı görünmeli
    
- Geçen süre görünmeli
    
- Ürünler ve modifier seçenekleri görünmeli
    
- Müşteri notu görünmeli
    
- Sipariş durumu değiştirilebilmeli
    
- Ürün bazında durum değiştirilebilmeli
    
- Birden fazla mutfak cihazı eş zamanlı çalışabilmeli
    

Örnek durum geçişleri:

- CONFIRMED → IN_PREPARATION
    
- IN_PREPARATION → READY
    
- READY → SERVED
    

Geçersiz durum geçişleri backend tarafından engellenmelidir.

Birden fazla mutfak cihazının aynı siparişi aynı anda güncellemesi durumunda veri tutarlılığı sağlanmalıdır.

Gelecekte mutfak istasyonları desteklenebilmelidir:

- Bar
    
- Sıcak mutfak
    
- Soğuk mutfak
    
- Tatlı
    
- Kahve
    

Ürünlerin belirli hazırlık istasyonlarına yönlendirilebilmesi için mimari genişletilebilir olmalıdır.

---

# 16. Kasa Ekranı

Kasa ekranında aktif masalar liste veya plan görünümünde gösterilecektir.

Her masa kartında en az:

- Masa adı
    
- Aktif oturum durumu
    
- Toplam sipariş tutarı
    
- Açık sipariş sayısı
    
- Son sipariş zamanı
    
- Ödeme durumu
    

görünmelidir.

Örnek:

- Masa X
    
- 1.240 TL
    
- 4 sipariş
    
- Aktif
    

Kasiyer masaya tıkladığında:

- Masadaki tüm siparişler
    
- Siparişi veren kullanıcı veya misafir
    
- Sipariş zamanı
    
- Ürünler
    
- Modifier seçenekleri
    
- Ürün fiyatları
    
- İptal edilen ürünler
    
- Toplam tutar
    
- Durum geçmişi
    

görüntülenmelidir.

Kasiyer:

- Siparişin tamamını iptal edebilmeli
    
- Belirli sipariş kalemlerini iptal edebilmeli
    
- İptal nedeni seçebilmeli veya yazabilmeli
    
- Yanlış iptalleri geri alamama veya yetkili onayı gibi kurallara tabi olabilmeli
    

Kasadan bir ürün iptal edildiğinde:

- OrderItem durumu CANCELLED olmalı
    
- Masa toplamı yeniden hesaplanmalı
    
- Müşteri ekranında ürün aktif siparişlerden kaldırılmalı veya iptal edildi olarak gösterilmeli
    
- Mutfak ekranına iptal eventi gitmeli
    
- Ürün hazırlanmaya başladıysa mutfakta dikkat çekici iptal uyarısı gösterilmeli
    
- Audit log oluşturulmalı
    

Finansal ve denetim gereksinimleri nedeniyle sipariş verisi fiziksel olarak silinmemelidir.

İptal edilen ürün, geçmiş ve audit kayıtlarında bulunmalıdır.

---

# 17. Gerçek Zamanlı İletişim

Aşağıdaki işlemler gerçek zamanlı güncellenmelidir:

- Yeni join request
    
- Join request kabul veya ret
    
- Katılımcının masaya eklenmesi
    
- Siparişin oluşturulması
    
- Siparişin 10 saniye içinde iptali
    
- Siparişin onaylanması
    
- Siparişin mutfağa düşmesi
    
- Mutfak durum değişiklikleri
    
- Kasadan ürün iptali
    
- Masa toplamının değişmesi
    
- Ürünün stokta tükenmesi
    
- Menü ürününün kullanılabilirlik değişimi
    
- Masa oturumunun kapanması
    

WebSocket veya Socket.IO kullanımı değerlendirilebilir.

Ancak gerçek zamanlı kanal, sistemin tek doğruluk kaynağı olmamalıdır.

Client bağlantıyı kaybedip yeniden bağlandığında:

1. Son bilinen event sequence veya version gönderilmeli.
    
2. Kaçırılan güncellemeler alınmalı veya state yeniden çekilmeli.
    
3. Client server state ile reconcile edilmelidir. burda zaten hesabı girili olucak gereksiz karmaşaya gerek var mı 

Realtime gateway stateless ve yatay ölçeklenebilir olmalıdır.

Birden fazla gateway instance için:

- Redis Pub/Sub
    
- Redis Streams
    
- Kafka
    
- NATS
    

gibi backplane seçenekleri değerlendirilmelidir.

WebSocket odaları için örnek yapılar:

- business:{businessId}
    
- branch:{branchId}
    
- kitchen:{branchId}
    
- cashier:{branchId}
    
- table-session:{tableSessionId}
    
- customer-session:{participantId}
    

Her odaya katılmadan önce authorization kontrolü yapılmalıdır.

Client tarafından gönderilen room ID'ye körü körüne güvenilmemelidir.

---

# 18. Asenkron ve Event-Driven Mimari

Aşağıdaki işlemler event tabanlı yapılabilir:

- İşletme oluşturuldu
    
- Varsayılan menü oluşturulması
    
- Şube oluşturuldu
    
- Şube davet e-postası gönderilmesi
    
- Menü ürünü güncellendi
    
- Şube ürün durumu değişti
    
- Masa oluşturuldu
    
- QR kod üretildi
    
- Masa oturumu açıldı
    
- Join request oluşturuldu
    
- Sipariş oluşturuldu
    
- Sipariş iptal süresi doldu
    
- Sipariş onaylandı
    
- Sipariş iptal edildi
    
- Sipariş kalemi iptal edildi
    
- Sipariş mutfağa gönderildi
    
- Sipariş hazırlandı
    
- Masa toplamı değişti
    
- Masa kapatıldı
    
- Analitik verisi güncellendi
    
- Bildirim oluşturuldu
    

Örnek event isimleri:

- BusinessCreated
    
- DefaultMenuProvisionRequested
    
- DefaultMenuProvisioned
    
- BranchCreated
    
- BranchInvitationRequested
    
- BranchEmailVerified
    
- MenuProductCreated
    
- MenuProductUpdated
    
- BranchProductAvailabilityChanged
    
- TableCreated
    
- TableQrGenerated
    
- TableSessionOpened
    
- TableJoinRequested
    
- TableJoinApproved
    
- TableJoinRejected
    
- OrderPlaced
    
- OrderCancellationWindowExpired
    
- OrderConfirmed
    
- OrderCancelledByCustomer
    
- OrderCancelledByCashier
    
- OrderItemCancelled
    
- OrderSentToKitchen
    
- OrderPreparationStarted
    
- OrderReady
    
- OrderServed
    
- TableTotalChanged
    
- TableSessionClosed
    

Her eventte en az:

- eventId
    
- eventType
    
- eventVersion
    
- occurredAt
    
- correlationId
    
- causationId
    
- producer
    
- tenantId veya businessId
    
- branchId
    
- aggregateId
    
- payload
    

alanları bulunmalıdır.

Event consumer'lar idempotent olmalıdır.

At-least-once delivery durumunda duplicate eventlerin zarar vermemesi sağlanmalıdır.

Transactional outbox pattern kullanılmasını değerlendir.

---

# 19. Önerilen Mikroservisler

Aşağıdaki servis sınırlarını değerlendir ve gerekiyorsa birleştir veya böl.

## 19.1 Identity Service

Sorumluluklar:

- Kayıt
    
- Giriş
    
- Google OAuth
    
- E-posta doğrulama
    
- Şifre sıfırlama
    
- Token yönetimi
    
- Refresh token
    
- Oturum ve cihaz yönetimi
    
- Kullanıcı profili
    

## 19.2 Tenant veya Business Service

Sorumluluklar:

- İşletme oluşturma
    
- İşletme üyelikleri
    
- İşletme rolleri
    
- İşletme ayarları
    

## 19.3 Branch Service

Sorumluluklar:

- Şube oluşturma
    
- Şube bilgileri
    
- Adres yönetimi
    
- Çalışma saatleri
    
- Şube üyelikleri
    
- Şube rolleri
    
- Şube e-posta değişikliği
    
- Şube sipariş kabul durumu
    

## 19.4 Catalog veya Menu Service

Sorumluluklar:

- Menü
    
- Kategoriler
    
- Ürünler
    
- İçerikler
    
- Modifier grupları
    
- Modifier seçenekleri
    
- Şube override kayıtları
    
- Şube ürün kullanılabilirliği
    

## 19.5 Media Service

Sorumluluklar:

- Presigned upload URL
    
- Görsel metadata
    
- Thumbnail işleme
    
- Dosya doğrulama
    
- Kullanılmayan görsellerin temizlenmesi
    

İlk aşamada bağımsız servis olmak zorunda olup olmadığını değerlendir.

## 19.6 Table Service

Sorumluluklar:

- Şube alanları
    
- Masalar
    
- QR tokenları
    
- Masa oturumları
    
- Masa katılımcıları
    
- Katılım istekleri
    
- Masa sahipliği
    

## 19.7 Cart Service

Sorumluluklar:

- Aktif sepet
    
- Sepet ürünleri
    
- Modifier seçimleri
    
- Sepet doğrulama
    

Cart Service'in ayrı servis mi yoksa Order Service içinde modül mü olması gerektiğini değerlendir.

## 19.8 Order Service

Sorumluluklar:

- Sipariş oluşturma
    
- Fiyat hesaplama
    
- Sipariş snapshotları
    
- 10 saniyelik iptal penceresi
    
- Sipariş durum makinesi
    
- Sipariş iptali
    
- Sipariş geçmişi
    
- Masa toplamının hesaplanması
    

## 19.9 Kitchen Service

Sorumluluklar:

- Mutfak iş listesi
    
- Hazırlık durumu
    
- Mutfak istasyonları
    
- Kitchen display projection
    

Bunun ayrı bir source-of-truth servisi olmak yerine Order eventlerinden beslenen read model olup olmaması gerektiğini değerlendir.

## 19.10 Cashier Service

Sorumluluklar:

- Aktif masaların kasa görünümü
    
- Masa toplamları
    
- Sipariş detay görünümü
    
- Yetkili iptal işlemleri
    
- Kasa projection/read model
    

Siparişlerin asıl sahibi Order Service olmalıdır. Cashier Service siparişi doğrudan kendi veritabanında değiştirmemelidir.

## 19.11 Realtime Gateway

Sorumluluklar:

- WebSocket bağlantıları
    
- Oda yönetimi
    
- Kullanıcı bağlantı eşlemesi
    
- Eventleri bağlı clientlara iletme
    
- Reconnect desteği
    

İş kurallarının Realtime Gateway içinde tutulmasından kaçınılmalıdır.

## 19.12 Notification Service

Sonraki aşama:

- Push notification
    
- E-posta
    
- SMS
    
- Uygulama içi bildirim
    
- Şube ve işletme uyarıları
    

## 19.13 Analytics Service

Sonraki aşama:

- Günlük satış
    
- Ürün performansı
    
- Saatlik yoğunluk
    
- Şube karşılaştırmaları
    
- İptal oranları
    
- Ortalama hazırlama süresi
    
- Ortalama masa süresi
    

Ana transaction veritabanında ağır analitik sorgular çalıştırılmamalıdır.

## 19.14 Payment Service

Sonraki aşama:

- Online ödeme
    
- Masa hesabı ödeme
    
- Bölünmüş ödeme
    
- İade
    
- Webhook
    
- Payment provider abstraction
    
- Ödeme idempotency
    
- Reconciliation
    

---

# 20. Veri Tabanı Stratejisi

Ana transactional veriler için ilişkisel veritabanı tercih edilmesi değerlendirilmelidir.

Önerilen:

- PostgreSQL
    

PostgreSQL için gerekçeler:

- Sipariş ve finansal kayıtların ilişkisel yapısı
    
- Transaction desteği
    
- Unique constraint
    
- Row locking
    
- JSONB desteği
    
- Güçlü sorgulama
    
- Partitioning
    
- Read replica
    
- PostGIS desteği
    

Redis şu amaçlarla kullanılabilir:

- Cache
    
- Rate limit
    
- Distributed lock
    
- Session verisi
    
- Kısa ömürlü join request verisi
    
- WebSocket backplane
    
- Job queue
    

Ancak siparişlerin tek kalıcı kaynağı Redis olmamalıdır.

Arama için başlangıçta PostgreSQL full-text yeterli olabilir. İleride:

- OpenSearch
    
- Elasticsearch
    

değerlendirilebilir.

Konum tabanlı restoran sorguları için:

- PostgreSQL PostGIS
    
- Geospatial index
    

kullanımı değerlendirilmelidir.

---

# 21. Temel Veri Modelleri

Aşağıdaki entityler için ayrıntılı şema oluştur:

- User
    
- IdentityProvider
    
- EmailVerification
    
- PasswordResetToken
    
- RefreshToken
    
- UserSession
    
- Business
    
- BusinessMember
    
- Branch
    
- BranchMember
    
- BranchInvitation
    
- Address
    
- BusinessHours
    
- Menu
    
- MenuCategory
    
- Product
    
- ProductImage
    
- Ingredient
    
- ProductIngredient
    
- ModifierGroup
    
- ModifierOption
    
- ProductModifierGroup
    
- BranchProductOverride
    
- BranchModifierOverride
    
- ServiceArea
    
- RestaurantTable
    
- TableQrToken
    
- TableSession
    
- TableParticipant
    
- TableJoinRequest
    
- Cart
    
- CartItem
    
- CartItemModifier
    
- Order
    
- OrderItem
    
- OrderItemModifier
    
- OrderStatusHistory
    
- OrderCancellation
    
- KitchenTicket
    
- KitchenTicketItem
    
- AuditLog
    
- OutboxEvent
    
- IdempotencyRecord
    

Her tablo için:

- Primary key
    
- Foreign key
    
- Unique constraint
    
- Indexler
    
- Tenant alanları
    
- Soft delete gereksinimi
    
- Version alanı
    
- createdAt ve updatedAt
    

belirtilmelidir.

ID stratejisi için UUIDv7, ULID veya benzeri sıralanabilir ve dağıtık sistemlere uygun kimlikler değerlendirilmelidir.

---

# 22. Sipariş Snapshot Stratejisi

Sipariş verildiği anda aşağıdaki bilgiler snapshot olarak OrderItem içinde tutulmalıdır:

- productId
    
- productName
    
- productDescription
    
- unitPrice
    
- quantity
    
- currency
    
- tax bilgisi
    
- selectedModifier isimleri
    
- selectedModifier fiyatları
    
- müşteri notu
    
- ürün görseli için opsiyonel snapshot URL
    
- calculatedTotal
    

Bu snapshot sayesinde:

- Menü ürünü silinse
    
- Ürün adı değişse
    
- Fiyat değişse
    
- Modifier silinse
    

bile geçmiş sipariş doğru kalmalıdır.

Para alanlarında floating-point kullanılmamalıdır.

Seçenekler:

- Kuruş cinsinden integer
    
- Decimal/Numeric
    

Para birimi ayrıca saklanmalıdır.

---

# 23. API Tasarım Gereksinimleri

API'ler versiyonlanmalıdır.

Örnek:

`/api/v1/...`

API Gateway üzerinden:

- Authentication
    
- Rate limiting
    
- Request ID
    
- Correlation ID
    
- CORS
    
- Genel input limiti
    
- Route forwarding
    
- Observability
    

sağlanabilir.

Ancak tüm authorization yalnızca gateway'de bırakılmamalıdır. Servisler de kaynak yetkisini doğrulamalıdır.

Örnek endpoint grupları oluştur:

## Auth

- POST /auth/register
    
- POST /auth/login
    
- POST /auth/google
    
- POST /auth/refresh
    
- POST /auth/logout
    
- POST /auth/logout-all
    
- POST /auth/email-verifications
    
- POST /auth/email-verifications/confirm
    
- POST /auth/password-resets
    
- POST /auth/password-resets/confirm
    

## Businesses

- POST /businesses
    
- GET /businesses/
    
- PATCH /businesses/
    
- GET /businesses//members
    
- POST /businesses//members
    

## Branches

- POST /businesses//branches
    
- GET /businesses//branches
    
- GET /branches/
    
- PATCH /branches/
    
- POST /branches//change-email
    
- POST /branches//verify-email
    

## Menus

- GET /businesses//menu
    
- POST /businesses//menu/categories
    
- POST /businesses//menu/products
    
- PATCH /products/
    
- DELETE /products/
    
- GET /branches//menu
    
- PATCH /branches//products//override
    
- PATCH /branches//products//availability
    

## Tables

- POST /branches//service-areas
    
- POST /branches//tables
    
- GET /branches//tables
    
- PATCH /tables/
    
- POST /tables//regenerate-qr
    
- GET /public/tables//context
    

## Table sessions

- POST /public/tables//sessions/join
    
- POST /table-sessions//join-requests
    
- POST /table-sessions//join-requests//approve
    
- POST /table-sessions//join-requests//reject
    
- POST /table-sessions//transfer-ownership
    
- POST /table-sessions//leave
    
- POST /table-sessions//close
    

## Cart

- GET /table-sessions//cart
    
- POST /table-sessions//cart/items
    
- PATCH /cart/items/
    
- DELETE /cart/items/
    

## Orders

- POST /table-sessions//orders
    
- GET /table-sessions//orders
    
- GET /orders/
    
- POST /orders//cancel
    
- POST /orders//items//cancel
    
- POST /orders//start-preparation
    
- POST /orders//ready
    
- POST /orders//serve
    

Endpointleri REST açısından değerlendir ve gerekiyorsa command endpointleri kullan.

Sipariş oluşturma endpointi idempotency key kabul etmelidir:

`Idempotency-Key: <unique-value>`

Aynı key ile tekrarlanan istek ikinci bir sipariş oluşturmamalıdır.

---

# 24. Tutarlılık ve Transaction Sınırları

Aşağıdaki işlemler güçlü transaction gerektirir:

- Sipariş oluşturma
    
- Sipariş kalemlerinin oluşturulması
    
- Sipariş toplamının hesaplanması
    
- Outbox event kaydının oluşturulması
    
- Müşterinin 10 saniye içinde iptali
    
- Kasa iptali
    
- Masa toplamı güncellemesinin kaynak verisi
    

Aşağıdaki işlemler eventual consistency kullanabilir:

- Mutfak ekranı projection
    
- Kasa ekranı projection
    
- Analitik
    
- Bildirim
    
- Arama indexi
    
- Menü cache
    
- WebSocket mesajı
    

Sipariş oluşturulduğu halde realtime mesaj gönderilemezse sipariş kaybolmamalıdır.

Veritabanı transactionı ile message broker publish işlemi arasındaki dual-write problemi çözülmelidir.

Transactional outbox pattern için ayrıntılı tasarım sun.

---

# 25. Cache Stratejisi

Cache için uygun adaylar:

- Şube menüsü
    
- Ürün detayları
    
- Şube çalışma saatleri
    
- İl, ilçe, mahalle listeleri
    
- İşletme temel bilgileri
    
- Yetki sorguları
    
- Aktif masa özetleri
    

Siparişin kesin durumu için cache tek doğruluk kaynağı olmamalıdır.

Cache key örnekleri:

- menu:branch:{branchId}
    
- branch:{branchId}
    
- address
    
- address:districts:{provinceId}
    
- permissions:user:{userId}:branch:{branchId}
    

Menü güncellendiğinde:

- Event yayınlanmalı
    
- İlgili cache invalidation yapılmalı
    
- Menü version artırılmalı
    
- Bağlı müşterilere yeni version bilgisi gönderilmeli
    

Cache stampede ve stale data senaryolarını değerlendir.

---

# 26. Yakındaki Restoranlar

Müşteri uygulaması açıldığında kullanıcıya yakındaki restoranlar gösterilecektir.

Akış:

1. Kullanıcıdan konum izni istenir.
    
2. İzin verilirse enlem ve boylam alınır.
    
3. Belirli yarıçap içindeki açık şubeler sorgulanır.
    
4. Mesafeye göre sıralanır.
    
5. Şube çalışma saatleri ve sipariş kabul durumu değerlendirilir.
    

Liste kartlarında:

- İşletme adı
    
- Şube adı
    
- Logo veya görsel
    
- Mesafe
    
- Açık veya kapalı durumu
    
- Tahmini yoğunluk için gelecekte genişletilebilir alan
    
- Mutfak veya kategori etiketleri
    
- Adres
    

bulunabilir.

Konum izni verilmezse:

- İl ve ilçe manuel seçimi
    
- Arama
    
- Daha önce seçilen konum
    

sunulmalıdır.

PostGIS kullanarak örnek geospatial sorgu ve index tasarımı oluştur.

Konum verisinin gereksiz yere kalıcı saklanmaması ve KVKK açısından değerlendirilmesi gerekir.

---

# 27. Güvenlik Gereksinimleri

En az aşağıdaki güvenlik kontrolleri bulunmalıdır:

- Argon2id veya güvenli parola hash algoritması
    
- Kısa ömürlü access token
    
- Refresh token rotation
    
- Refresh token reuse detection
    
- HttpOnly, Secure ve SameSite cookie seçenekleri
    
- CSRF koruması
    
- OAuth state ve PKCE
    
- E-posta tokenlarının hashlenerek saklanması
    
- Şifre sıfırlama tokenlarının tek kullanımlık olması
    
- Rate limiting
    
- Login brute-force koruması
    
- Account enumeration önleme
    
- Input validation
    
- SQL injection koruması
    
- XSS koruması
    
- Dosya yükleme güvenliği
    
- Tenant isolation
    
- WebSocket authentication
    
- Room authorization
    
- Audit logging
    
- Secret management
    
- TLS
    
- Hassas log verilerinin maskelenmesi
    
- Backup encryption
    
- Admin işlemleri için güçlü yetkilendirme
    

Google Maps linki kullanıcı girdisi olduğu için URL doğrulaması ve güvenli çıktı encoding uygulanmalıdır.

QR tokenlar tahmin edilemez olmalıdır.

Müşteri, branchId veya businessId değiştirerek başka tenant verilerine erişememelidir.

---

# 28. Audit Log

Aşağıdaki işlemler audit log oluşturmalıdır:

- İşletme bilgilerinin değiştirilmesi
    
- Şube oluşturma ve silme
    
- Şube e-postasının değiştirilmesi
    
- Rol değişiklikleri
    
- Menü fiyat değişikliği
    
- Ürün silme veya pasife alma
    
- Stok durumunun değiştirilmesi
    
- Masa QR kodunun yenilenmesi
    
- Kasadan sipariş iptali
    
- Sipariş kalemi iptali
    
- Masa oturumunun personel tarafından kapatılması
    
- Ödeme ve iade işlemleri
    

Audit log alanları:

- actorUserId
    
- actorType
    
- businessId
    
- branchId
    
- action
    
- resourceType
    
- resourceId
    
- before
    
- after
    
- IP
    
- userAgent
    
- requestId
    
- occurredAt
    

Audit kayıtları normal kullanıcı tarafından değiştirilememelidir.

---

# 29. Hata Yönetimi

Tüm servisler standart hata formatı kullanmalıdır.

Örnek:

```json
{
  "error": {
    "code": "ORDER_CANCELLATION_WINDOW_EXPIRED",
    "message": "Siparişin doğrudan iptal süresi doldu.",
    "details": {},
    "requestId": "req_..."
  }
}
```

Örnek hata kodları:

- AUTH_INVALID_CREDENTIALS
    
- EMAIL_NOT_VERIFIED
    
- TENANT_ACCESS_DENIED
    
- BRANCH_ACCESS_DENIED
    
- PRODUCT_NOT_AVAILABLE
    
- PRODUCT_OUT_OF_STOCK
    
- INVALID_MODIFIER_SELECTION
    
- TABLE_SESSION_NOT_ACTIVE
    
- TABLE_JOIN_APPROVAL_REQUIRED
    
- ORDER_ALREADY_CREATED
    
- ORDER_CANCELLATION_WINDOW_EXPIRED
    
- ORDER_ALREADY_CANCELLED
    
- INVALID_ORDER_STATUS_TRANSITION
    
- BRANCH_NOT_ACCEPTING_ORDERS
    
- CONCURRENT_UPDATE_CONFLICT
    
- RATE_LIMIT_EXCEEDED
    

Retry edilebilir ve edilemez hatalar ayrılmalıdır.

---

# 30. Yüksek Trafik ve Ölçeklenme

Yoğun saatlerde şu trafik türleri artacaktır:

- QR taramaları
    
- Menü görüntüleme
    
- Sepet güncellemeleri
    
- Sipariş oluşturma
    
- WebSocket bağlantıları
    
- Mutfak ekranı eventleri
    
- Kasa ekranı sorguları
    

Tasarımdaki bileşenler stateless ve yatay ölçeklenebilir olmalıdır.

Önerilen teknikler:

- Load balancer
    
- Container orchestration
    
- Horizontal autoscaling
    
- Read replica
    
- Database connection pooling
    
- PgBouncer
    
- Redis cluster veya managed Redis
    
- Broker partitioning
    
- CDN
    
- Object storage
    
- Backpressure
    
- Circuit breaker
    
- Timeout
    
- Retry with exponential backoff
    
- Bulkhead isolation
    
- Dead-letter queue
    
- Graceful shutdown
    

Order eventlerinde partition key olarak branchId veya orderId kullanılmasını değerlendir.

Aynı siparişe ait eventlerin sıralı işlenmesi gereksinimini açıkla.

Bir şubenin aşırı trafiğinin diğer işletmeleri etkilememesi için tenant bazlı rate limit ve quota stratejisi oluştur.

---

# 31. Dayanıklılık ve Hata Senaryoları

Aşağıdaki senaryolar için sistem davranışını tasarla:

1. Sipariş veritabanına kaydedildi fakat message broker erişilemiyor.
    
2. Sipariş onay eventi iki kere teslim edildi.
    
3. Mutfak ekranı internet bağlantısını kaybetti.
    
4. Kasa ekranı yeniden bağlandı.
    
5. Redis tamamen erişilemez oldu.
    
6. Bir servis yeniden başlatıldı.
    
7. Kullanıcı sipariş butonuna iki kere bastı.
    
8. Kullanıcının iki farklı cihazı aynı siparişi iptal etti.
    
9. Şube ürünü stokta yok yaptı fakat müşteri eski menüyü görüyor.
    
10. Sipariş oluşturulurken ürün fiyatı değişti.
    
11. Masa sahibi uygulamayı kapattı.
    
12. Join request onaylanırken oturum kapandı.
    
13. Şube hesabının e-postası değiştirildiği sırada eski kullanıcı giriş yapmaya çalıştı.
    
14. İşletme veya şube pasife alındı.
    
15. QR kod başka bir yerde paylaşıldı.
    
16. Eventlerin sırası bozuldu.
    
17. Bir projection eventleri geriden takip ediyor.
    
18. Veritabanı primary node'u çöktü.
    
19. Üçüncü taraf görsel servisi erişilemez oldu.
    
20. Türkiye adres API'si erişilemez oldu.
    

Her senaryo için:

- Beklenen kullanıcı deneyimi
    
- Veri tutarlılığı
    
- Retry davranışı
    
- Log ve alert
    
- Manuel müdahale gerekip gerekmediği
    

belirtilmelidir.

---

# 32. Gözlemlenebilirlik

Sistem aşağıdaki gözlemlenebilirlik bileşenlerini içermelidir:

- Structured logging
    
- Centralized log aggregation
    
- Metrics
    
- Distributed tracing
    
- Correlation ID
    
- Request ID
    
- Event ID
    
- Health check
    
- Readiness check
    
- Liveness check
    
- Alerting
    

OpenTelemetry kullanımı değerlendirilmelidir.

Temel metricler:

- Request latency
    
- Error rate
    
- Orders per minute
    
- Order confirmation delay
    
- Event consumer lag
    
- WebSocket active connections
    
- Queue depth
    
- Failed jobs
    
- Database connection usage
    
- Cache hit rate
    
- Sipariş iptal oranı
    
- Mutfak hazırlama süresi
    
- Şube başına aktif masa sayısı
    

Siparişin API'den mutfak ekranına ulaşmasına kadar geçen süre ölçülebilmelidir.

---

# 33. Bildirim Sistemi

Sonraki sürümde desteklenecek bildirimler:

## Müşteri

- Masaya katılım isteği
    
- Katılım kabul edildi
    
- Katılım reddedildi
    
- Sipariş onaylandı
    
- Sipariş hazırlanmaya başladı
    
- Sipariş hazır
    
- Sipariş kalemi iptal edildi
    
- Ödeme istendi
    
- Masa kapatıldı
    

## Şube

- Yeni sipariş
    
- Uzun süredir bekleyen sipariş
    
- İptal edilen sipariş
    
- Ürün stokta tükendi
    
- Sistem veya ödeme uyarısı
    

## İşletme

- Şube çevrimdışı
    
- Yüksek iptal oranı
    
- Kritik operasyon uyarısı
    
- Günlük satış özeti
    

Notification Service kanal bağımsız tasarlanmalıdır:

- In-app
    
- Push
    
- E-posta
    
- SMS
    

Bildirim tercihleri kullanıcı bazında saklanabilmelidir.

---

# 34. Analitik Sistemi

Analitik sistemi transactional order tablolarına ağır sorgu yükü bindirmemelidir.

Eventlerden beslenen analitik pipeline tasarla.

İleride gösterilecek metrikler:

- Günlük, haftalık ve aylık satış
    
- Şube bazlı satış
    
- Ürün bazlı satış
    
- En çok satan ürünler
    
- En düşük performanslı ürünler
    
- Ortalama sipariş tutarı
    
- Saatlik yoğunluk
    
- Günlere göre yoğunluk
    
- Sipariş iptal oranı
    
- İptal nedenleri
    
- Ortalama hazırlama süresi
    
- Masa devir süresi
    
- Stokta yok kalma süreleri
    
- Yeni ve tekrar gelen müşteri oranı
    
- Şube karşılaştırması
    

Başlangıçta PostgreSQL read model, daha sonra ClickHouse, BigQuery, Redshift veya benzeri analitik sistemlere geçiş seçeneğini değerlendir.

---

# 35. Ödeme Sistemine Hazırlık

Ödeme ilk MVP'de bulunmayacaktır.

Ancak sipariş ve masa modeli gelecekte şunları desteklemelidir:

- Masanın tamamını ödeme
    
- Kendi siparişlerini ödeme
    
- Hesabı kişiler arasında bölme
    
- Ürün bazında bölme
    
- Tutar bazında bölme
    
- Online kartla ödeme
    
- Kasada ödeme
    
- Nakit
    
- Birden fazla ödeme yöntemi
    
- Bahşiş
    
- İade
    
- Kısmi iade
    
- Başarısız ödeme
    
- Pending ödeme
    
- Payment webhook
    
- Reconciliation
    

Order durumu ile Payment durumu birbirinden ayrılmalıdır.

Siparişin hazırlanması ve ödeme durumunun aynı state machine içinde karıştırılmaması gerekir.

---

# 36. Teknoloji Yığını

Aşağıdaki veya daha uygun alternatifleri değerlendir:

## Backend

- TypeScript
    
- Node.js
    
- NestJS veya Fastify tabanlı yapı
    

Alternatif:

- Java ve Spring Boot
    
- Go
    

Takımın hızlı geliştirme yapabilmesi ile yüksek trafik ihtiyacını birlikte değerlendir.

## Web frontend

- React
    
- TypeScript
    
- Vite veya Next.js
    

Müşteri restoran keşif sayfaları için SEO gerekiyorsa Next.js değerlendir.

Kasa ve mutfak ekranları için PWA desteğini değerlendir.

## Mobil

Daha sonra:

- React Native
    
- Flutter
    
- Native uygulamalar
    

## Veritabanı

- PostgreSQL
    
- PostGIS
    
- Redis
    

## Message broker

Şunları karşılaştır:

- RabbitMQ
    
- Apache Kafka
    
- NATS JetStream
    
- AWS SQS/SNS
    
- Google Pub/Sub
    

MVP ve büyük ölçek için ayrı öneri ver.

## Gerçek zamanlı iletişim

- WebSocket
    
- Socket.IO
    
- SSE'nin uygun olduğu alanlar
    

## Altyapı

- Docker
    
- Kubernetes veya başlangıçta managed container platform
    
- Terraform
    
- GitHub Actions
    
- OpenTelemetry
    
- Prometheus
    
- Grafana
    
- Loki veya ELK
    
- Sentry
    

Küçük ekip için aşırı operasyonel yük oluşturmayacak başlangıç mimarisi öner.

---

# 37. Deployment Ortamları

En az şu ortamlar bulunmalıdır:

- Local
    
- Development
    
- Staging
    
- Production
    

Her ortamda:

- Ayrı veritabanı
    
- Ayrı cache
    
- Ayrı message broker namespace
    
- Ayrı object storage bucket veya prefix
    
- Ayrı OAuth credential
    
- Ayrı secrets
    

bulunmalıdır.

Production secretları repository'de tutulmamalıdır.

Database migration stratejisi oluşturulmalıdır.

Backward-compatible deployment ve event schema versioning açıklanmalıdır.

---

# 38. Test Stratejisi

Şu test türlerini planla:

- Unit test
    
- Integration test
    
- Contract test
    
- API test
    
- End-to-end test
    
- WebSocket test
    
- Event consumer test
    
- Load test
    
- Security test
    
- Failure injection test
    
- Migration test
    

Özellikle şu akışlar test edilmelidir:

1. Aynı sipariş isteğinin iki kez gönderilmesi
    
2. 10 saniye dolmadan iptal
    
3. 10 saniye dolduktan sonra iptal
    
4. Sipariş onayı ve iptal yarış koşulu
    
5. Duplicate event
    
6. Out-of-order event
    
7. Stokta olmayan ürün siparişi
    
8. Fiyatı değişen ürün
    
9. Yetkisiz tenant erişimi
    
10. Yetkisiz WebSocket room erişimi
    
11. Aynı masaya birden fazla katılım
    
12. Masa sahibinin bağlantısının kopması
    
13. Kasa iptalinin müşteriye yansıması
    
14. Mutfak ekranının reconnect olması
    

Load test için senaryo oluştur:

- 10.000 eş zamanlı müşteri
    
- 2.000 aktif masa
    
- 1.000 aktif WebSocket bağlantısı veya daha yüksek hedef
    
- Belirli sürede yoğun sipariş patlaması
    
- Aynı şubede yüksek trafik
    
- Çok sayıda küçük şubenin eş zamanlı kullanımı
    

Gerçek kapasite hedefleri varsayım olarak belirtilmeli ve benchmark ile doğrulanmalıdır.

---

# 39. MVP Kapsamı

İlk MVP için önerilen kapsam:

## Dahil

- İşletme kaydı
    
- E-posta doğrulama
    
- Google ile giriş
    
- Şube oluşturma
    
- Şube e-posta doğrulama
    
- Türkiye adres seçimi
    
- İşletme menüsü
    
- Şube menü override
    
- Görsel yükleme
    
- Ürün ve modifier yönetimi
    
- Anlık stokta var/yok
    
- Şube alanları ve masalar
    
- Kalıcı QR kod
    
- Guest müşteri oturumu
    
- Masa oturumu
    
- Masa sahibi
    
- Katılım onayı
    
- Sepet
    
- Sipariş oluşturma
    
- 10 saniyelik iptal penceresi
    
- Mutfak ekranı
    
- Kasa ekranı
    
- Kasadan iptal
    
- WebSocket güncellemeleri
    
- Temel audit log
    

## Sonraki sürüme bırakılabilecekler

- Online ödeme
    
- Gelişmiş analitik
    
- Push notification
    
- SMS
    
- Sadakat sistemi
    
- Kupon
    
- Rezervasyon
    
- Kurye
    
- Hammadde bazlı stok
    
- Mutfak istasyonları
    
- Gelişmiş çalışan vardiya sistemi
    
- Çoklu dil
    
- Çoklu para birimi
    
- Mobil uygulamalar
    

---

# 40. Önerilen Geliştirme Aşamaları

## Faz 0: Mimari temel

- Monorepo
    
- Ortak kod standartları
    
- CI/CD
    
- Docker
    
- Authentication altyapısı
    
- API Gateway
    
- PostgreSQL
    
- Redis
    
- Message broker
    
- Observability temeli
    

## Faz 1: İşletme ve şube

- Kullanıcı kaydı
    
- Google OAuth
    
- İşletme oluşturma
    
- Şube oluşturma
    
- E-posta doğrulama
    
- Rol ve yetki sistemi
    
- Adres sistemi
    

## Faz 2: Menü

- Varsayılan menü
    
- Kategoriler
    
- Ürünler
    
- Görseller
    
- İçerikler
    
- Modifier sistemi
    
- Şube override
    
- Stokta var/yok
    

## Faz 3: Masa ve QR

- Alan yönetimi
    
- Masa yönetimi
    
- QR üretimi
    
- Masa session
    
- Guest session
    
- Masa sahibi
    
- Join request
    

## Faz 4: Sipariş

- Sepet
    
- Fiyat doğrulama
    
- Sipariş snapshot
    
- Idempotency
    
- 10 saniyelik iptal
    
- Delayed job
    
- Order state machine
    

## Faz 5: Operasyon ekranları

- Mutfak ekranı
    
- Kasa ekranı
    
- WebSocket
    
- Reconnect
    
- Kasadan iptal
    
- Audit log
    

## Faz 6: Ölçek ve dayanıklılık

- Outbox
    
- Retry
    
- DLQ
    
- Cache
    
- Load test
    
- Tracing
    
- Alerting
    
- Read models
    

## Faz 7: Müşteri keşif

- Yakındaki restoranlar
    
- PostGIS
    
- Şube listeleme
    
- Konum izni
    
- Manuel şehir seçimi
    

## Faz 8: Mobil, analitik ve ödeme

- React Native veya Flutter
    
- Push notification
    
- Analytics pipeline
    
- Online ödeme
    

---

# 41. Karar Verilmesi Gereken Ürün Soruları

Bu soruların her biri için:

- Önerilen varsayılan kararı ver.
    
- Alternatifleri açıkla.
    
- Seçimin mimariye etkisini belirt.
    

## Hesaplar

1. Şubeler ortak tek hesap mı kullanacak, çalışanların ayrı hesapları mı olacak?
    
2. İşletme sahibi aynı zamanda müşteri hesabıyla da giriş yapabilecek mi?
    
3. Müşteri hesap oluşturmadan sipariş verebilecek mi?
    
4. Telefon numarası doğrulaması gerekli mi?
    
5. Şube e-postası gerçek bir kullanıcı hesabı mı, yoksa davet adresi mi olacak?
    

## Masa sistemi

6. Şube personeli masayı önceden açmak zorunda mı?
    
7. Müşteri QR okuttuğunda masa otomatik açılacak mı?
    
8. Masa oturumu ne zaman otomatik kapanacak?
    
9. Masa sahibi uygulamadan çıkarsa ne olacak?
    
10. Masa sahibi join request'i cevaplamazsa personel müdahale edebilecek mi?
    
11. Aynı kişi başka masaya geçebilir mi?
    
12. Aynı cihaz birden fazla masada aktif olabilir mi?
    

## Sipariş

13. Her müşteri yalnızca kendi siparişini mi iptal edebilir?
    
14. Masa sahibi diğer müşterilerin siparişini iptal edebilir mi?
    
15. Müşteri 10 saniye içinde tüm siparişi mi, ürün bazında mı iptal edebilir?
    
16. 10 saniye sonunda mutfağa topluca mı, ürün bazında mı gönderilecek?
    
17. Şube siparişi reddedebilir mi?
    
18. Mutfak ürün kalemini reddedebilir mi?
    
19. Sipariş hazırlandıktan sonra kasa iptali yapılabilecek mi?
    
20. İptal nedeni zorunlu olacak mı?
    

## Menü

21. Fiyat şube bazında değişebilir mi?
    
22. Şube merkezi ürünü tamamen silebilir mi, yoksa sadece gizleyebilir mi?
    
23. İşletme ana ürünü silerse şube override ne olacak?
    
24. Ürün farklı saatlerde aktif olabilir mi?
    
25. Ürün adet stoğu ilk sürümde gerekli mi?
    
26. Tek ürüne birden fazla görsel eklenebilir mi?
    
27. Ürünün porsiyon veya boyut seçenekleri olacak mı?
    

## Adres ve keşif

28. Daire numarası gerçekten her şube için zorunlu mu?
    
29. Kullanıcının girdiği Google Maps linkinden koordinat çıkarılacak mı?
    
30. Konum izni vermeyen kullanıcı restoranları nasıl görecek?
    
31. Restoranların hangi yarıçap içinde gösterileceği sabit mi olacak?
    

## Operasyon

32. Kasa ve mutfak ekranları aynı hesapla mı açılacak?
    
33. Mutfak ve kasa için ayrı permission gerekli mi?
    
34. Şube personeli hangi siparişi kimin iptal ettiğini görecek mi?
    
35. Şube interneti kesildiğinde offline çalışma isteniyor mu?
    
36. Menü değişiklikleri anında mı yayınlanacak, taslak ve yayınlama sistemi mi olacak?
    

## Ticari model

37. İşletmeler abonelikle mi kullanılacak?
    
38. Şube sayısına göre ücret olacak mı?
    
39. Sipariş başına komisyon olacak mı?
    
40. Ücretsiz deneme süresi olacak mı?
    
41. Platform yöneticisi işletme hesaplarını askıya alabilecek mi?
    

---

# 42. İlk Sürüm İçin Varsayımlar

Cevap verilmemiş noktalar için şu varsayımlarla tasarım yap:

- Müşteriler hesap açmadan guest olarak sipariş verebilir.
    
- Şubeler başlangıçta ortak hesap kullanabilir.
    
- Uzun vadede çalışan bazlı hesap sistemine geçilir.
    
- Şube personeli masayı önceden açmak zorunda değildir.
    
- İlk QR tarayan müşteri masa oturumunu otomatik açar.
    
- Masa sahibi yalnızca katılım isteklerini yönetir.
    
- Masa sahibi diğer kişilerin siparişlerini iptal edemez.
    
- Her müşteri yalnızca kendi siparişini ilk 10 saniyede iptal edebilir.
    
- 10 saniye sonunda sipariş mutfağa gönderilir.
    
- Kasiyer süre sonrasında sipariş veya kalem iptal edebilir
    
- Şube fiyat override yapabilir.
    
- Şube merkezi ürünü silemez, yalnızca gizleyebilir.
    
- İlk sürümde adet bazlı stok yoktur.
    
- Ürün için birden fazla görsel desteklenir.
    
- Modifier grupları desteklenir.
    
- Daire numarası opsiyoneldir.
    
- Açık adres ayrıntısı zorunludur.
    
- Yakındaki restoranlar varsayılan olarak 10 kilometre yarıçapında gösterilir.
    
- Offline sipariş kabul edilmez.
    
- Bağlantı kesildiğinde sepet cihazda geçici tutulabilir.
    
- Sipariş server onayı olmadan başarılı sayılmaz.
    
- Menü değişiklikleri MVP'de doğrudan yayınlanır.
    
- Sonraki sürümde taslak ve yayınlama sistemi eklenebilir.
    

---

# 43. Beklenen Çıktı Formatı

Cevabını aşağıdaki sırayla üret:

1. Yönetici özeti
    
2. Gereksinim analizi
    
3. Belirsizlikler ve kabul edilen varsayımlar
    
4. Modüler monolit ve mikroservis karşılaştırması
    
5. Önerilen nihai mimari
    
6. C4 Context Diagram
    
7. C4 Container Diagram
    
8. Mikroservis listesi ve sınırları
    
9. Servisler arası bağımlılık matrisi
    
10. Senkron iletişim tablosu
    
11. Asenkron event tablosu
    
12. Message broker seçimi
    
13. Veritabanı stratejisi
    
14. Ayrıntılı entity ve tablo şemaları
    
15. Index ve constraint önerileri
    
16. API endpoint tasarımı
    
17. Authentication ve authorization tasarımı
    
18. QR ve masa session güvenliği
    
19. Sipariş state machine
    
20. OrderItem state machine
    
21. 10 saniyelik iptal mekanizması
    
22. Transactional outbox tasarımı
    
23. Idempotency tasarımı
    
24. WebSocket ve reconnect tasarımı
    
25. Cache stratejisi
    
26. Medya depolama stratejisi
    
27. Türkiye adres sistemi
    
28. Yakındaki restoran sorgusu
    
29. Audit ve güvenlik
    
30. Hata senaryoları
    
31. Ölçeklendirme
    
32. Observability
    
33. Deployment mimarisi
    
34. Test stratejisi
    
35. MVP kapsamı
    
36. Fazlara ayrılmış geliştirme planı
    
37. Önerilen monorepo klasör yapısı
    
38. İlk geliştirilecek servis ve modüller
    
39. Teknik riskler
    
40. Ürün sahibine sorulması gereken kalan sorular
    

Tüm diyagramları Mermaid formatında yaz.

Tablo şemalarında alan tiplerini belirt.

Event payloadları için JSON örnekleri ver.

API endpointleri için request ve response örnekleri ver.

Sipariş, QR masa katılımı ve kasa iptali için sequence diagram oluştur.

Karar verirken “ileride yapılabilir” şeklinde belirsiz cevaplar verme. MVP için net bir teknoloji ve mimari seç, daha büyük ölçek için geçiş yolunu ayrıca açıkla.

---

# 44. Özel Teknik İlkeler

Tasarıma şu ilkeleri uygula:

- Database per service hedefi
    
- Transactional outbox
    
- Idempotent consumers
    
- At-least-once delivery varsayımı
    
- Optimistic concurrency
    
- API versioning
    
- Event schema versioning
    
- Zero-trust tenant authorization
    
- Immutable order snapshots
    
- Soft delete yalnızca uygun entitylerde
    
- Finansal ve sipariş kayıtlarında fiziksel silme yapılmaması
    
- Para hesaplarında floating-point kullanılmaması
    
- Client zamanına güvenilmemesi
    
- Realtime kanalın source of truth olmaması
    
- Durable delayed jobs
    
- Stateless backend
    
- Graceful degradation
    
- Observability by default
    
- Secure-by-default
    
- Mobile-ready API design
    
- Backward-compatible migration
    
- Contract testing
    

Çözüm, yalnızca teorik bir mimari çizimi değil, geliştirilmeye başlanabilecek kadar somut bir teknik tasarım olmalıdır.