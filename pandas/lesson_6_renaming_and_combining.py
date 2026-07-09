import pandas as pd 

wine_frame = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

print("incase index names seems nonsense pandas has a method to change them" \
"u can use rename method and who the hell is using points as a score")
wine_frame.rename(columns = {'points':'score'},inplace=True)
print(wine_frame.columns)

print("we can use indexes to change indexes names but I dont think I am gonna use it")

wine_frame.rename(index={0: 'firstEntry', 1: 'secondEntry'},inplace=True)
# instad of index it says ulke how funny
print(wine_frame.head(3)) # firstEntry,secondEntry,2,3,4...

first_frame = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Ali", "Veli", "Ayşe"],
    "score": [80, 90, 75]
})

second_frame = pd.DataFrame({
    "student_id": [1, 2, 4],
    "city": ["İstanbul", "Ankara", "İzmir"],
    "score": [85, 95, 70]
})

print("I am gonaa use these two to understand things")


print(first_frame)
print(second_frame)

print("change score to final_score")
first_frame.rename(columns={'score': 'final_score'}, inplace=True)
second_frame.rename(columns={'score': 'final_score'}, inplace=True)

print("concat add the same column name to the same column name and" \
" same row index to the same row index")
print(pd.concat([first_frame, second_frame], axis=0, ignore_index=True)) # axis=0 means row wise concatenation
print("*"*50)
print("first frame has name second dont so second frame get all Na values")


side_by_side = pd.concat([first_frame, second_frame], axis=1)
first_indexed = first_frame.set_index("student_id")
second_indexed = second_frame.set_index("student_id")

print(first_indexed)
print(second_indexed)

joined_frame = first_indexed.join(second_indexed,    lsuffix="_df1",
    rsuffix="_df2",
    how="outer")
print(joined_frame)

print("join makes the same thinh with sql but u cant specify the join column its " \
"index by default but u can use merge for it I dont have a df for it now but its " \
"the same thinh with sql join ")