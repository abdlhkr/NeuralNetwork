import matplotlib.pyplot as plt
import numpy as np


# all the things we will make with matplotlib first we create a figure and an axis

""" figure = plt.figure()
axis = plt.axes()
x = np.linspace(0, 10, 1000)
axis.plot(x, np.sin(x))
plt.show()

plt.plot(x, np.sin(x))
plt.show()


plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show() """


""" print("*"*50)
print("we can change color by adding color argument to plot function")
x = np.arange(0, 10, 2)
y = np.arange(0, 10, 2)**2
plt.plot(x,y,color='blue')
print("plot function takes two arguments first one is x and second one is y"
"if we give only one argument x will be default 1,2,3... and y will be the argument")
print("some crazy ways to add a color to the graph")
plt.show()
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
plt.plot(y,color='orange',marker='o')
print("marker adds a point to the graph at each data point")

plt.show()
 """
x = np.arange(0, 10, 2)
y = np.arange(0, 10, 2)**2
print("*"*50)
""" print("we can change the line style by linestyle argument " \
"solid , dashed , dashdot , dotted")
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted')
plt.show() """

print("we can use xlim and ylim to chose the range of x and y axis")
print("it seems like a good way to manipulate results in a period")
plt.xlim(10, 0)
plt.ylim(0, 64)
plt.plot(x,y,color='#FFDD44',marker='o')
plt.show()


x = np.linspace(0, 1000, 120)
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5]) # we can specify xlim and ylim with axis 
# same as 
#plt.xlim(-1, 11)
#plt.ylim(-1.5, 1.5)
plt.show()


print(" you can also use tight to automatically adjust the axis limits to fit the data")
print("this is  golden")
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.tight_layout()
plt.show()


print("we can define title x axis name y axis name ")

plt.title("sinus function")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, np.sin(x))
plt.show()


plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')

plt.legend() # that adds a label about wich line is which
plt.show() # its useful when we have multiple lines in a graph


x = np.arange(0, 10, 2)
y = np.arange(0, 10, 2)**3
y_v2 = np.arange(0, 10, 2)**2
plt.plot(x,y,color = 'red',linestyle = 'solid',label = 'y = x^3')
plt.plot(x,y_v2,color = 'blue',linestyle = 'dashed',label = 'y = x^2')

plt.legend()
plt.show()

print("")

ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot')

plt.show()


print("scattered plots is the same thing only there isn't" \
"a line that connect points lets see")
plt.plot(x, y, 'o', color='black')
plt.show()



rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    # example of each scattered symbols
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)
plt.show()


