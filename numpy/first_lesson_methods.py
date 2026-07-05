import numpy as np
import matplotlib.pyplot as plt
# to be able to create a virtual env for python code is 
array = [1, 2, 1] #  has one axis. That axis has 3 elements in it,
print(array)
print(type(array))
array = np.array(array)
print(type(array))
print(array)

print("*"*20)

second_array = [[1., 0., 0.],[0., 1., 2.]]
print(second_array)
print(type(second_array))
second_array = np.array(second_array)
print(type(second_array)) 
print(second_array) # first diffrencecs is that its readble like a matrix

# NumPy’s array class is called ndarray thats why all type gave same answer

# SOME METHODS FOR ndarrays 

print("arrray is : " , array)
print("ndim gives number of dimensions: ", array.ndim) # number of axes (dimensions) of the array. In this case, it is 1
print("shape gives shape of array: ", array.shape) # shape of the array. In this case, it is (3,) which means that it has 3 elements in one axis
print("size gives total elements in the array: ", array.size) # size gives total elements in the array. In this case, it is 3
print("DTYPE gives data type of the array: ", array.dtype) # dtype gives data type of the array. In this case, it is int64
print("itemsize give the size of a single element in the array: ", array.itemsize) # itemsize gives the size of a single element in the array. In this case, it is 8 bytes 
# the reason its 64 bit 8 byte is my system is 64 bit and numpy gives dtype according to the system architecture. If it was 32 bit it would have given 4 bytes 
print(array.data) # .data gives pointer to the first element of the array 
print("*"*50)
print("second array is : " , second_array)
print("ndim gives number of dimensions: ", second_array.ndim) # number of axes (dimensions) of the array. In this case, it is 2
print("shape gives shape of second array: ", second_array.shape) # shape of the array. In this case, it is (2, 3) which means that it has 2 axes and each axis has 3 elements in it
print("size gives total elements in the second array: ", second_array.size) # size gives total elements in the array. In this case, it is 6
print("DTYPE gives data type of the second array: ", second_array.dtype) # dtype gives data type of the array. In this case, it is float64
print("itemsize give the size of a single element in the second array: ", second_array.itemsize) # itemsize gives the size of a single element in the array. In this case, it is 8 bytes
print("the reason dtype gives diffrents result is second array has commas and " \
"numpy gives automatic data type to the array based on the elements in" \
" it. In this case," \
" it is float64 because it has float elements in it and int 64 because my" \
" system works on 64 bit architecture and numpy gives dtype according to the " \
"system architecture. If it was 32 bit it would have given 4 bytes ")


