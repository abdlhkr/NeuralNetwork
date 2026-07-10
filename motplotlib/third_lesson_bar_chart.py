from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import font_manager as fm
import pandas as pd
import numpy as np

experience = [1,2,3,4,5,6,7,8]

data_scientists_salary = [6500, 9280, 12050, 13200, 16672, 21000, 23965, 29793]

software_engineers_salary = [9020, 12873, 15725, 18000, 19790, 20196, 25769,32000 ]


print("standart usage of bar same as plot and same arguments x y labels etc")
plt.bar(experience,data_scientists_salary,color="b")

plt.title("Salary of Data Scientists")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.tight_layout()
plt.grid(False)

plt.show()

print("*"*50)
print("we can combine bar and line plot in the same graph" \
" by calling plot and bar function together it seems terrible don't use it often")

plt.bar(experience,data_scientists_salary,color="r", label= "Data Scientists")
plt.plot(experience,software_engineers_salary, color="g",label= "Software Engineers" )

plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.legend()
plt.grid(False)

plt.show()

print("*"*50)
print("we can change the width of the bars but default seems better usually")

plt.bar(experience,data_scientists_salary,width=0.5,color="r", label= "Data Scientists")
plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

print("*"*50)
print("u can use plt.grid(True) but it seems terrible don't use it '")

print("*"*50)
print("we can add multiple bars ")
print("the way it works is first one takes bottom and " \
"second one takes top and show how much more it is than the first one")

plt.bar(experience,software_engineers_salary, color="g",linewidth=3,label= "Software Engineers" )
plt.bar(experience,data_scientists_salary,color="r",linewidth=3, label= "Data Scientists")

plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.legend()
plt.grid(False)

plt.show()


print("*"*50)



experience_indexes = np.arange(len(experience))

plt.style.use("fivethirtyeight")

width = 0.4

plt.bar(experience_indexes - width,software_engineers_salary, color="g",width=width,linewidth=3,label= "Software Engineers" )
plt.bar(experience_indexes+width,data_scientists_salary,color="r",linewidth=3,width=width, label= "Data Scientists")

plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.legend()
plt.grid(False)

plt.show()

print("*"*50)
print("I couldn't understand the difffrence other then width ")

width = 0.25

plt.bar(experience_indexes - width,software_engineers_salary, color="g",width=width,linewidth=3,label= "Software Engineers" )
plt.bar(experience_indexes+width,data_scientists_salary,color="r",linewidth=3,width=width, label= "Data Scientists")

plt.title("Salary of Data Scientists and Software Engineers by their experiences")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.xticks(ticks=experience_indexes)

plt.legend()
plt.grid(True)

plt.show()