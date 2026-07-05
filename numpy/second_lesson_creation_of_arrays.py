import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
import sys

# there are several ways to create an array in numpy. Some of them are:
# u can create an array from a python list just like last lesson
array = [1,2,3] 
numpy_array = np.array(array) # this is the most common way 
numpy_array = np.array([1,2,3]) # this is also a common way and the same thing as above
# to create an array in numpy. It takes a python list as input
#  and returns a numpy array

# array transforms sequences of sequences into two-dimensional arrays,
#  sequences of sequences of sequences into three-dimensional arrays, and so on.
three_dimensional_array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Three-dimensional array:") #  (2, 2, 3) iki blok var her blokta 2 satır var
# ve her satırda 3 sütun var gibi düşün
print(three_dimensional_array)
print("Shape of three-dimensional array:", three_dimensional_array.shape)
print("Number of dimensions:", three_dimensional_array.ndim)

print("we can specify the data type of the array while creating it using dtype parameter")
numpy_array = np.array([1, 2, 3], dtype=np.float64)
print("Array with specified data type:", numpy_array)
print("Data type of the array:", numpy_array.dtype)
print("it should be int64 if it created without specifying the data")

print("*"*100)
print("\n"*3)
print("numpy has zeros and ondes to create a specific shape of array with all zeros or ones")
zeros_array = np.zeros((2,3))
print("Zeros array:")
print(zeros_array)
ones_array = np.ones((2,3))
print("Ones array:")
print(ones_array)

print("arrange gives three arguments start, stop and step and returns an array with values from start to stop with step")
arranged_array = np.arange(0, 10, 2)
print("Arranged array: starts from 0 to 10 with step 2", arranged_array)
print("just like range function it doesn't count the last value ")
print("it also accepts float values")
arranged_array = np.arange(0.0, 10.0, 1.8)
print("Arranged array: starts from 0.0 to 10.0 with step 1.8", arranged_array)
print("if you onlt give one argumenrt it will be considered as stop and " \
"start will be 0 and step will be 1")

print("line space makes excatly the same thing as arrange but " \
"instead of step it takes number of elements from the last argument ")

print("unlike arrange linespace includes the last element ")
line_space_array = np.linspace(0, 1, 11)
print("Line space array: starts from 0 to 1 with 11 elements", line_space_array)

""" x = np.linspace(0, 2 * pi, 100)
print("Line space array: starts from 0 to 2*pi with 100 elements", x) 
I might not use it soon"""


# reshpe method takes element of an array and reshapes it into a new shape. The new shape must have the same number of elements as the original array.

default_arranged_array = np.arange(12)
print("Default arranged array: ", default_arranged_array)
reshaped_array = default_arranged_array.reshape(3, 4)
print("Reshaped array: ")
print(reshaped_array)
three_dimensional_reshaped_array = default_arranged_array.reshape(2, 2, 3)
print("Three-dimensional reshaped array: ")
print(three_dimensional_reshaped_array)


print(np.arange(99999)) # instead of writing each element just start and end 
# we can change this behaviur by
np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported
# print(np.arange(99999)) # now it will print all the elements in the array
# DO NOT DO TT UNLESS SOMETHİNG WEIRD

# arithmetic operations performs just like normal 
normal_array = np.array([1, 2, 3, 4])
normal_array = normal_array.reshape(2, 2)
print("Normal array: ")
print(normal_array)
normal_array2 = np.array([5, 6, 7, 8])
normal_array2 = normal_array2.reshape(2, 2)
print("Normal array 2: ")
print(normal_array2)

print("sum of two arrays: ")
print(normal_array + normal_array2)

print("subtraction of two arrays: ")
print(normal_array - normal_array2)

print("square of first array: ")
print(normal_array ** 2)

print("subtract constant from array :normal array - 1")
print(normal_array - 1)

print("random.rand creates an array of given shape elements with random values between 0 and 1")
random_array = np.random.rand(2, 3) # random array with shape (2, 3)
print("Random array: ")
print(random_array)
print(random_array*10 < 6)

print("* sign works element wise in numpy lets say ")
one_array = np.ones((2, 2))
random_array = np.random.rand(2, 2)
print("Random array: ")
print(random_array)
print("multiplication of two arrays: ")
print(random_array * one_array)

print("for matrix multiplication we can use @ sign or dot method")
print(one_array @ random_array)
print(one_array.dot(random_array))
print("lets make values easier for us to see")
first_array = np.arange(4)
first_array = first_array.reshape(2, 2)
print("First array: " )
print(first_array)
second_array = np.arange(4, 8)
second_array = second_array.reshape(2, 2)
print("Second array: ")
print(second_array)
print("Matrix multiplication of two arrays: ")  
print(first_array @ second_array)
print(second_array.dot(first_array))


rg = np.random.default_rng(1) # one is seed value. It is used to initialize the
# random number generator. If you use the same seed value, you will get the same
#  random numbers every time you run the code. This is useful for debugging and
#  testing purposes.
a = np.ones((2, 3), dtype=np.int_)
b = rg.random((2, 3))
print("b: ", b)
a *= 3
print("a: ", a)
b+= a
print("b: ", b)

# whike doing operation dtype will change to biggest data type in the operation
# its like c 
print("first array: ")
print(first_array)
print("ndarrays also has sum min max mean methods")
print("Sum: ", np.sum(first_array))
print("Min: ", np.min(first_array))
print("Max: ", np.max(first_array))
print("Mean: ", np.mean(first_array))

print("u can specify the axis to perform these operations ")
print("Sum along axis 0: ", np.sum(first_array, axis=0))
print("Sum along axis 1: ", np.sum(first_array, axis=1))


# there are sun functions called universal functions (ufuncs) in numpy.
#  They are functions that operate on ndarrays element-wise. Some of the 
# most common ufuncs are:

normal_array = np.array([1, 2, 3, np.pi / 2]).reshape(2, 2)
print("normal array:")
print(normal_array)

print("exp function: ", np.exp(normal_array))
print("sqrt function: ", np.sqrt(normal_array))
print("sin function: ", np.sin(normal_array)) # sin function takes input in radians
# not degrees