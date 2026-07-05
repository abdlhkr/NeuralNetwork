import numpy as np 
import matplotlib.pyplot as plt

# One-dimensional arrays can be indexed, sliced and
#  iterated over, much like lists and other Python sequences.
# ONE DİMENSIONAL ARRAY
array = np.arange(10) ** 3
print("One-dimensional array: ")
print(array)

print("u can make operation just like a normal list  ")
print("second element of the array: ", array[1])
print("from 3 to 5 element of the array: ", array[2:5])
print("start to finish by step 2: ", array[::2])

array[::2] = 99 # makes every second element of the array 99
print("array after changing every second element to 99: ")
print(array) 
print("to reverse the array use [::-1]")
print("reversed array: ", array[::-1])

def f (x, y):
    return 10 * x + y

new_array = np.fromfunction(f, (5, 4), dtype=np.int_)
# fromfunction = Construct an array by executing a function over each coordinate.
# 00 01 02 03
# 10 11 12 13 ...
print(new_array)

print("second element of the third row: ", new_array[2, 1])
print(new_array[0:5, 1])
print("thats the same as all columns first row wich also can be written as ")
print(new_array[:,1])
print(new_array[0:5, 2])
print(new_array[0:5, 1:3])
print(new_array[:, 1:3])
# When fewer indices are provided than the number of axes,
#  the missing indices are considered complete slices :
print(new_array[:])
print(new_array[1]) # second row of the array
print(new_array[-1]) # same as new_array[-1,:]

for row in new_array:
    print(row) # prints each row of the array

for element in new_array.flat:
    print(element) # prints each element of the array
