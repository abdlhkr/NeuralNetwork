from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import font_manager as fm
import pandas as pd
import numpy as np
from datetime import datetime, timedelta #It's for time series

# I actually finf a better source so I will be using it from now on


print("line plot is the most common type of plot in data ")

experience = [1,3,4,5,7,8,10,12]

salary = [6500, 9280, 12050, 13200, 16672, 21000, 23965, 29793]


print("plot function takes two arguments first is x and second is y")
print("inorder to show a plot u should use .show() function")
plt.plot(experience,salary)
plt.show()

print("*"*50)

print("u can add a title to graph")

x_axis = np.arange(-10,10)
y_axis = np.arange(-10,10)**2
plt.plot(x_axis,y_axis)
plt.title("square of numbers")
plt.show()

print("*"*50)

print("we can add labels to axises such as xlabel and ylabel")

x_axis = np.arange(-10,10)
y_axis = np.arange(-10,10)**2
plt.plot(x_axis,y_axis)
plt.title("square of numbers")
plt.xlabel("numbers")
plt.ylabel("square of numbers")
plt.show()



print("*"*50)
print("we can add multiple lines to the same graph " \
"by calling plot function multiple times")
print("we can add labels to each line by legend function")

experience = [1,3,4,5,7,8,10,12]

data_scientists_salary = [6500, 9280, 12050, 13200, 16672, 21000, 23965, 29793]

software_engineers_salary = [9020, 12873, 15725, 18000, 19790, 20196, 25769,32000 ]

plt.plot(experience,data_scientists_salary)
plt.plot(experience,software_engineers_salary)

plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")
# loc specify the location it offen gives automatically really good 
plt.legend(["Data Scientists Salary","Software Engineers Salary"], loc="upper left")
plt.show()

print("*"*50)

print("if you add labels to each plot u dont have to specify them in legend function")


experience = [1,3,4,5,7,8,10,12]

data_scientists_salary = [6500, 9280, 12050, 13200, 16672, 21000, 23965, 29793]

software_engineers_salary = [9020, 12873, 15725, 18000, 19790, 20196, 25769,32000 ]

plt.plot(experience,data_scientists_salary, label="Data Scientists Salary")
plt.plot(experience,software_engineers_salary, label="Software Engineers Salary")

plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")
# loc specify the location it offen gives automatically really good 
plt.legend()
plt.show()


print("*"*50)

print("we can make line different")
plt.plot(experience,data_scientists_salary, label="Data Scientists Salary",linestyle="--")
plt.plot(experience,software_engineers_salary, label="Software Engineers Salary")

plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")
# loc specify the location it offen gives automatically really good 
plt.legend()
plt.show()

print("*"*50)

print("marker points each x and y point in the graph")

plt.plot(experience,data_scientists_salary, label="Data Scientists Salary",linestyle="--", marker="o")
plt.plot(experience,software_engineers_salary, label="Software Engineers Salary", marker="s")
plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")
# loc specify the location it offen gives automatically really good 
plt.legend()
plt.show()

print("We can also adjust line width by using linewidth argument." \
"but I don't think that would be necessary lets see")


plt.plot(experience,data_scientists_salary,linewidth = 5, label="Data Scientists Salary",linestyle="--", marker="o")
plt.plot(experience,software_engineers_salary, linewidth = 2, label="Software Engineers Salary", marker="s")
plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")
# loc specify the location it offen gives automatically really good 
plt.legend()
plt.show()

print("we can use tight_layout() function to make sure that the labels and titles" \
" are not cut off in the graph")

plt.plot(experience,data_scientists_salary,linewidth = 5, label="Data Scientists Salary",linestyle="--", marker="o")
plt.plot(experience,software_engineers_salary, linewidth = 2, label="Software Engineers Salary", marker="s")
plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.show()

print("*"*50)

print("by specifying plt.grid(True) we can add grid to the graph")
plt.plot(experience,data_scientists_salary,linewidth = 5, label="Data Scientists Salary",linestyle="--", marker="o")
plt.plot(experience,software_engineers_salary, linewidth = 2, label="Software Engineers Salary", marker="s")
plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()


print("*"*50)

print("stackplot takes the same arguments as plot function but it adds the " \
"ability to create stacked area plots")

plt.stackplot(
    experience,
    data_scientists_salary,
    labels=[
        "Data Scientist"    ],
    colors=["red", "blue", "green"]
)

plt.legend(loc="upper left")
plt.show()

print("*"*50)

print("it's time to see bar charts we use it with plt.bar() function")

x = ["A", "B", "C", "D"]
y = [3, 8, 1, 10]
plt.bar(x, y)
plt.show()