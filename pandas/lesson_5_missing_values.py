import pandas as pd 


wine_frame = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)


print(wine_frame.columns)
print("we can use dtype for each column")

print("data type of the price column : ",wine_frame.price.dtype)

print("we can use it at the dataframe level to see all data types of the columns")
print(wine_frame.dtypes)

print("*"*50)

print("we can use astype to conver dtype of a column to another type")

# int_prices = wine_frame['price'] = wine_frame['price'].astype('int64')
print("if there are none or inf values casting to int wont work instead")
int_prices = pd.to_numeric(wine_frame.price,errors='coerce').astype('Int64')
# we can use Int64 instead of int64 to allow for NaN values
print(wine_frame.price.head(5))
print(int_prices.head(5))

print("*"*50)
print("we can select none values by using pd.isnull(df['column_name']) or df['column_name'].isnull()")
is_country_null = pd.isnull(wine_frame.country)
null_country = wine_frame[is_country_null]
print("empty country values :",null_country)

print("*"*50)
print("there are some operations to fill the none values")
print("one of them is fillna() method")

wine_frame['region_2_filled'] = wine_frame.region_2.fillna("Unknown")
print("at first glance putting unknown in the none values seems nonsense but" \
"there is a benefit group by works unknown values as a group instead passing them" \
" as none values")
print(wine_frame.region_2_filled.head(5))

print("*"*50)
print("instead of filling with constant values we can use ffill or bfill" \
" methods to fill the none values with the previous or next values")

filled_region_2 = wine_frame.region_2.bfill()
print(filled_region_2.head(5))

print("forward fill has some disatvantages for example if the first value"
" is none it will stay none because there is no previous value to fill it with")

filled_region_2 = wine_frame.region_2.ffill() 
print(filled_region_2.head(5))


print("*"*50)
print("there could be valıes that is not null but replaced through the time" \
"lets say  reviewer Kerin O'Keefe has changed her Twitter handle from"
" @kerinokeefe to @kerino")

changed_twitter_handle = wine_frame['taster_twitter_handle'].replace("@kerinokeefe","@kerino")
print(changed_twitter_handle.head(5))


print("sum counts true as 1 and false as 0 so we can use it to learn" \
"how many none values are in a column")
n_missing_prices = wine_frame.price.isnull().sum()
print("Number of missing prices:", n_missing_prices)
