import numpy as np 
import matplotlib.pyplot as plt

print("broadcasting is if you making matrix operations on different sized arrays," \
" numpy will automatically expand the smaller array to match the size of the larger" \
" array it only works if the smaller array can be broadcast to the larger array," \
" meaning that the smaller array's dimensions must be compatible with the larger array's dimensions")

big_array = np.array([[1, 2, 3], [4, 5, 6]])
small_array = np.array([10, 20, 30])
# smaller act like it is [[10, 20, 30], [10, 20, 30]] and then add them together
print(big_array + small_array)

print("to be able to use broadcasting dimensions must be same or one of them must be 1,"
" if they are not compatible it will throw an error")

print("ADVANCED INDEXİNG")


square_array = np.arange(12)**2
print("square array: ", square_array)

print("normally u can reach any index by array[index] u can also give it a list " \
"lets try ")
index_list =np.array([1, 1, 3, 8, 5])
print("index list: ", index_list)
print(square_array[index_list])

print("thats a bit tricky but u can also give bidimensional array as index ")

bidemensional_index_array = np.array([[1, 1], [3, 8]])
print("bidimensional index array: ", bidemensional_index_array)
print(square_array[bidemensional_index_array]) # that gives us 2*2 

print("while pointing multidimensional array first index refers to the first dimension")

palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white

image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])

# index array is two dimension so each value in the index array corresponds 
# to a row in the palette array

print(palette[image])  # the (2, 4, 3) color image

a = np.arange(12).reshape(3, 4)
print(a)
i = np.array([[0, 1], [1, 2]]) # indice for first dimension
j = np.array([[2, 1], [3, 3]]) # indice for second dimension

# these indeces act like you hstack them [0,2], [1,1], [1,3], [2,3] and then get the values of those indeces

print(a[i, j])  # the result of indexing with arrays i and j
print(a[i, 0])  # the result of indexing with array i and a scalar index
print("***"*20)


time = np.linspace(20, 145, 5,dtype=int)  # time scale
data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
print(data)

max_index = data.argmax(axis=0)  # index of the maximum value for each series
print(max_index)


print("***"*20)
print("we can use boolean arrays to index an array and pick elements")
a = np.arange(12).reshape(3, 4)
print(a)
b = a > 4
print(b)
print(a[b])
a[b] = 0 # all elements that are greater than 4 will be set to 0
print(a)

normal_array = np.arange(12).reshape(3, 4)
print(normal_array)
b1 = np.array([False, True, True])         # first dim selection
b2 = np.array([True, False, True, False])  # second dim selection
print(normal_array[b1])  # index with first boolean array
print(normal_array[:, b2])  # index with second boolean array
print("the reason that doesnt give us 2*2 is numpy turns them into numbers")
print("b1 turns to [1, 2] and b2 turns to [0, 2] so it gives us " \
"[normal_array[1, 0], normal_array[2, 2]]")
print(normal_array[b1, b2])  # index with both boolean arrays