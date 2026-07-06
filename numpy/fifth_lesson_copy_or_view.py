import numpy as np 
import matplotlib.pyplot as plt

print("this part about if created a new copy" \
"or we just created a view of the original array" \
"so if we change the view it will change the original array as well")

simple_array = np.array([[1, 2, 3], [4, 5, 6]])
print("original array: ", simple_array)
copy_array = simple_array


print("is operator checks if two variables point to the same object in memory")
print("are they the same object? ", simple_array is copy_array)

print("function calls doesn't create a new object, they just return a" \
" reference to the original object so a change will affect the original " \
"object as well")

def change_array(arr):
    arr += 1  

print("simple array before change: ", simple_array)
change_array(simple_array)
print("make shure to check if u need original array after the method ")
print("simple array after change: ", simple_array)


print("there is a weird method let's say u need the same data change accordingly" \
"but call it with different name u can change and both will change thats view method")

simple_array = np.array([1, 2, 3])
view_array = simple_array.view()
print("original array: ", simple_array)
print("view array: ", view_array)
print("are they the same object? ", simple_array is view_array)
print("are they pointing to the same data? ", np.shares_memory(simple_array, view_array))
simple_array[1] = 100
print("original array after change: ", simple_array)
print("view array after change: ", view_array)
print("may be I lack some knowledge but thats the most stupid method I have ever seen")

simple_array = np.array([1, 2, 3, 4])
view_array = simple_array.view()
simple_array = simple_array.reshape((2, 2))

print("view array after reshaping the original array: ", view_array)
print("view genelde data belleğini paylaşır, ama metadata kendi başına olabilir.")
print("that means not all attributes shared among the view and the original array," \
" but they share the same data in memory now it seems more dumber then before")

a = np.array([[0, 10, 10, 3],
              [1234, 10, 10, 7],
              [8, 10, 10, 11]])
d = a.copy()  # a new array object with new data is created
print("d is a:", d is a)
print("d.base is a:", d.base is a)  # d doesn't share anything with a

print("d[0, 0] = 9999")
d[0, 0] = 9999
print("a:")
print(a)
print("copy is straightforward, you clone the data including the metadata " \
"to another array. and point it with another variable anychange wont affect the original array")


