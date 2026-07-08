import pandas as pd 
import numpy as np


wine_frame = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
print(wine_frame.head())
print("we can reach attribute names of a dataframe with columns")
print(wine_frame.columns)
print("to reach only one column we can use dot notation or bracket notation")
print(wine_frame.country.head())
print("we can reach it just like a dictionary with bracket notation")
print(wine_frame['country'].head())
print("do not forget that each column is a series so we can use series methods on it")

print("since a column is a series we can use indexing magic")
print(wine_frame.country[5:10])

#  However, pandas has its own accessor operators, loc and iloc. For more
#  advanced operations, these are the ones you're supposed to be using.

print(wine_frame.iloc[0]) # when we take only one row its like a series and readble
print(wine_frame.iloc[0:2]) # if u try to take more than one row it will be a
# dataframe and not readable
print("the way iloc works is first parameter is row and second parameter is column")
print("so to take first column value of a dataframe")
print(wine_frame.iloc[:,0]) # it's the same as 
print(wine_frame.country) # wich is the first column of the dataframe

print("first three country \n")
print(wine_frame.iloc[:3, 0])

print("instead of giving range we can give a list of indexes to take")
index_array = np.arange(0, 100, 5)
print(wine_frame.iloc[index_array, 0])
print("negative indexing also works with iloc ")

print("last two country values \n")
print(wine_frame.iloc[-2:, 0])

print("last row of the dataframe \n")
print(wine_frame.iloc[-1])

print("the diffrence between loc and iloc is that loc takes the" \
" index name and iloc takes the index number lets see")
print("*"*50)
print(wine_frame.loc[0]) # same as wine_frame.iloc[0] First row of the dataframe
print("*"*50)
print(wine_frame.loc[0:2, 'country']) # it will take the first three rows of country column 
# same as wine_frame.iloc[0:3, 0] but the difference is that loc takes the
#  index name and iloc takes the index number

print("*"*50)
print(wine_frame.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])
# selecting multiple columns with loc we can give a list of column names to take
# its easier then working with iloc in that regard

print("*"*50)
print("iloc[0:10] gives rows from position 0 to 9 and excludes 10.")
print("loc[0:10] gives rows with index labels from 0 to 10 and includes 10.")
print("This difference is important when working with string indexes. For example," \
" df.loc['potatoes':'tomatoes'] includes the 'tomatoes' index label, but iloc cannot" \
" use string labels because it works with integer positions.")

print("we can change the index of a dataframe with set_index method")
wine_frame.set_index("title", inplace=False)
# we can use it if we have a column with unique values and we want to use it as index of the dataframe
print(wine_frame.head())


print("lets say you wanna learn wines that produced in italy that takes less then 5 point")
produced_in_italy_takes_less_point = wine_frame.loc[(wine_frame.country == 'Italy') & (wine_frame.points < 5)]
# or takes higher then 90 points
print(wine_frame.loc[(wine_frame.country == 'Italy') & (wine_frame.points >= 90)])


print("***" * 50)

print("lets say you wanna see wines that produced in italy or takes more then average")
print(wine_frame.loc[(wine_frame.country == 'Italy') | (wine_frame.points > wine_frame.points.mean())])

print("if you have more then one option that will be included lets say" \
" Italy and France")
normal_frame = wine_frame.loc[(wine_frame.country == 'Italy') | (wine_frame.country == 'France')]
print("we can use isin method to make it easier")
is_in_frame = wine_frame.loc[wine_frame.country.isin(['Italy', 'France'])]
print("the point is isin method makes job easier when dealing with multiple choices")
print("lets see if they give the same result : ",normal_frame.equals(is_in_frame))

print("u can see null or not null values with isnull and notnull methods")
print(wine_frame.loc[wine_frame.price.isnull()].price) # all NaN
print(wine_frame.loc[wine_frame.price.notnull()].price) 

print("u can simply assign a new column for each row with assign method")
wine_frame['critic'] = 'everyone'
print(wine_frame.head().critic)
print("""%95 of your time u will be using loc top_oceania_wines = reviews.loc[(reviews.country.isin([\"Australia\",\"New Zealand\"])) & (reviews.points >= 95)]
""")