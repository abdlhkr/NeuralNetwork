import pandas as pd 

invoice_frame = pd.read_csv('pandas_apply_map_practice.csv', index_col=0)
print(invoice_frame.columns)
print("*"*50)
print(invoice_frame.head())

region_map = {
    "Istanbul": "Marmara",
    "Ankara": "İç Anadolu",
    "Izmir": "Ege",
    "Bursa": "Marmara"
}
invoice_frame['region'] = invoice_frame['city'].map(region_map)

print(invoice_frame.head())  
print(invoice_frame.tail()) # if key doesnt exist in the map value will be NaN

print("*"*50)
invoice_frame["member_label"] = invoice_frame["is_member"].map({True: "Member", False: "Non-Member"})
print(invoice_frame.head())

print("*"*50)

invoice_frame['total_amount'] = invoice_frame.apply((lambda row: row['quantity'] * row['unit_price']), axis=1)

print(invoice_frame.head())
print(invoice_frame.tail())
print("*"*50)


invoice_frame['total_discount'] = invoice_frame.apply((lambda row: row['total_amount'] * row['discount_rate']),axis = 1)

print(invoice_frame['total_discount'].head())
print("*"*50)   

print(invoice_frame[['product','quantity','total_discount']].head())


print("*"*50)   







