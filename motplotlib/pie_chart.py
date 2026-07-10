from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import font_manager as fm
import pandas as pd
import numpy as np


experience = [1,2,3,4,5,6,7,8]

data_scientists_salary = [6500, 9280, 12050, 13200, 16672, 21000, 23965, 29793]

software_engineers_salary = [9020, 12873, 15725, 18000, 19790, 20196, 25769,32000 ]


print("example chart instead of giving plot or bar we give them a pie" \
"plt.pie()")

plt.title("Pie Chart Example")

slices = [60,40]

plt.pie(slices)

plt.show()

print("*"*50)

print("we don't have to give total of 100 it will calculate the percentage automatically")

list_1 = [40,56,72,38,4]

plt.pie(list_1)

plt.show()

print("*"*50)

print("since we don't have an axis we add labels to every slice")
print("first slice start from the x axis and goes counter clockwise")
incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

plt.pie(incomes,labels=persons)

plt.show()

print("*"*50)
print("we can change the start angle of the first slice by startangle argument")


incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

plt.pie(incomes,labels=persons,startangle=90)

plt.show()

print("*"*50)
print("we can stand one of the slices out by explode argument")

incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

plt.pie(incomes,labels=persons,startangle=90,explode=(0,0.2,0,0,0))

plt.show()

print("*"*50)
print("we can stand more then one slice out " \
"explode parameter stands for radius of the slice 0.1 means 10% of the radius out" \
"but it seems like a bad idea to stand more than one slice out")

incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

plt.pie(incomes,labels=persons,startangle=90,explode=(0,0.2,0,0,0.4))

plt.show()

print("*"*50)

print("we can change the figure size by figsize argument in plt.figure() function" \
"that's a useful one at least for me  " \
"default figure size is (6.4, 4.8) so you can scale it up to your needs")

plt.figure(figsize=(10,10))

plt.rcParams['font.size'] = 20

incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

myexplode = [0,0.2, 0, 0, 0]

plt.pie(incomes,labels=persons,startangle=180,explode = myexplode)

plt.show()


print("*"*50)
print("we can add a shadow to the pie chart by shadow argument" \
"it doesn't seems to be necessary")


plt.figure(figsize=(10,10))

plt.rcParams['font.size'] = 20

incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

plt.pie(incomes,labels=persons,startangle=180,shadow = True,explode = (0,0.2, 0, 0, 0))

plt.show()

print("*"*50)
print("we can specify the colors of the slices by colors argument" )
print("for reference Default colors is nice ")


plt.figure(figsize=(10,10))

plt.rcParams['font.size'] = 20

incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

myexplode = [0,0.2, 0, 0, 0]

colors = ["black","g","y","hotpink","#4CAF70"]

plt.pie(incomes,labels=persons,startangle=180,explode = myexplode,shadow=True,colors=colors)

plt.show()

print("*"*50)
print("legend function also works here always use loc='best'" \
" it will find the best location for the legend")
plt.figure(figsize=(7,7))

incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

colors = ["black","g","y","hotpink","#4CAF70"]

plt.pie(incomes,labels=persons,colors=colors)
plt.legend(loc="best",title="Legend",fontsize=10)
plt.show()

print("*"*50)
print("we can show percentages on the pie chart" \
" by using autopct argument")

plt.figure(figsize=(7,7))

incomes = [40,56,72,38,4]

persons = ["Josh","Berkay","Maria","Michael","Anastacia"]

colors = ["black","g","y","hotpink","#4CAF70"]

plt.pie(incomes,labels=persons,colors=colors,autopct='%1.1f%%')
# %1.1f%% important part is .1f it means show 1 decimal point after
#  the number and % is for percentage sign
plt.legend(loc="best",title="Legend",fontsize=10)
plt.show()

