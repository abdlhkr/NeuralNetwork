import pandas as pd 

# to see each column in a dataframe we can set the display width to None.ve 
pd.set_option("display.width", None)         # genişlik sınırını kaldır
pd.set_option('display.max_rows', 5)        # make maximum rows to display 5
# There are two core objects in pandas: the DataFrame and the Series.

first_frame = pd.DataFrame({"yes":[50,21], "no":[131,2]})
# yes and no became column names 
print(first_frame)

string_frame = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(string_frame)

print("we can name indexes for better readability ")
readable_frame = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
                              'Sue': ['Pretty good.', 'Bland.']},
                             index=['Product A', 'Product B'])
print("we can't give more index names then the number of rows in the DataFrame")
print(readable_frame)

print("unlike a dataframe series is one dimensional arrays just like normal lists")
print("we can give data type just like numpy ")
first_series = pd.Series([1,2,3,4,5],dtype='float32')
print(first_series)

print("a series is just a column of a dataframe so we can assign labels just like frames ")
labeled_series = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(labeled_series)

print("we can create a frame from a csv file")

csv_frame = pd.read_csv('first_lesson.csv')
print(csv_frame)

real_csv_frame = pd.read_csv('winemag-data-130k-v2.csv')
print(real_csv_frame)

print(real_csv_frame.shape) # [129971 rows x 14 columns] it's a big one 

print(real_csv_frame.head())
# we actually have an index column and df also adding one we can say to use
# that index column as index
indexed_csv_frame = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
print(indexed_csv_frame.head())

print("importance of this lesson is index wich we can give a name to each row") 
print("also we can give a name to a series itself with name parameter")
print("dataframename.to_csv('filename.csv') to save a dataframe to csv file")