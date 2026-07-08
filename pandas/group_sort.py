import pandas as pd 


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
wine_frame = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)


print(wine_frame.columns)
print("group by makes exactly the same thing with sql group by")


print(wine_frame.groupby('country').price.mean())
print("*"*50)


print(" we can use apply in the same line with groupby")

#    print(wine_frame.groupby('winery').apply(lambda df: df.title.iloc[0]))

print("*"*50)

print("we can use more then one column or group by lets see")

print(wine_frame.groupby(['country','province']).price.max()) # province means şehir 

print("*"*50)
print(wine_frame.groupby(['country','province']).apply((lambda df : df.price.max())))
# the reeason we use df instead of row in the lambda function after groupby
# pandas takes each group as a dataframe and then we can apply any function
#  to that dataframe

print("*"*50)
print(wine_frame.groupby(['country']).price.agg(['mean','max','min']).sort_values('max')) # we can use multiple aggregation functions with agg method

print("*"*50)
print("instead of saying descending we use ascending = False")

print(wine_frame.groupby(['country']).price.agg(['mean','max','min']).sort_values('max',ascending = False))


print("*"*50)
print(".size() returns the size of each group")
print(wine_frame.groupby(['country']).size())

