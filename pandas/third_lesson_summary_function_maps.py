import pandas as pd 
import matplotlib.pyplot as plt
# there are summary functions to understand data easily lets see

wine_frame = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

print( "to see a columns values count avg std min max we can use describe method")
print("*"*50)
print(wine_frame.points.describe())
print("*"*50)
print("describe gets meaningless for string columns lets see")
print(wine_frame.country.describe()) # maybe uniqe but other than that meaningless

print("*"*50)
print("speaking of unique values we can use unique method to see them")
print(wine_frame.country.unique())
print("*"*50)
print("there are other functions that we can use in a column such as count, mean, std, min, max, sum, median, mode, quantile")
print("quantile gives us values that are useful for drawing boxplots")
print(wine_frame.points.quantile(0.25)) # 25% of the data is below this value
print("*"*50)
print("while loking around I find something we can draw boxplots with pandas")
# boxplot = wine_frame.boxplot(column='points', by='country', figsize=(12, 6)) # boxplot of points by country

plt.boxplot(wine_frame.points)
plt.title('Boxplot of Points')
plt.xlabel('Points')
plt.ylabel('Frequency')
# plt.show(),


print("*"*50)
print(".counts method gives unique values and their counts in a series")
print(wine_frame.country.value_counts())
print("I thought franch people have amazing wines it seems us won this time")
print("*"*50)
print("know its time for map functions it is a way to apply a function to each element in a series")
print("lets say if points > 90 its S grade and > 80 is A grade")

print("it seems like these wines are graded really highly lets see how many of them are graded S")
wine_frame['grade'] = wine_frame.points.map(lambda x: 'S' if x > 90 else ('A' if x > 80 else ('B' if x > 75 else 'F')))

print(wine_frame.grade.value_counts())

print("*"*50)

print("now just make mean of the points 0")
wine_frame_zero_mean = wine_frame.points.map(lambda point: point - wine_frame.points.mean())
print(wine_frame_zero_mean.mean()) # 0.0
print("I really never thought that I will be handling flowing points in a dataframe")

print("map should expect a single value and from the series and returs a series")

def remean_points(row,review_points_mean):
    row.points = row.points - review_points_mean
    return row

new_frame = wine_frame.apply(remean_points,axis=1, args=(wine_frame.points.mean(),))
print(new_frame.points.mean()) # 0.0
print(new_frame.points.head())

print("*"*50)
print("map and apply makes the same thing but we can use apply to work with multiple columns and rows")
print("in this example we worked with multiple columns in same row we cant do that with map" \
"" \
"also there is a problem with apply if there isnt a value for given situation it will return NaN" \
" u can use replace if u dont wanna see NaN values in your dataframe")
def wine_value_label(row):
    if row["points"] >= 90 and row["price"] <= 20:
        return "great deal"
    elif row["points"] >= 90:
        return "high quality"
    else:
        return "normal"

wine_frame["value_label"] = wine_frame.apply(wine_value_label, axis=1)

print(wine_frame[["points", "price", "value_label"]].head(10))

print("both apply and map doesn't change the original value unless we assign it ")

