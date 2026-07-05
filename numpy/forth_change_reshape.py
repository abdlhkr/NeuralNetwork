import numpy as np
import matplotlib.pyplot as plt



rg = np.random.default_rng(1)
a = np.floor(10 * rg.random((3, 4)))
print("a: ", a)

print("u can make an array flattened with ravel method")
print(a.ravel())
print(a.shape)
print(a.reshape(4,3))
print(a.reshape(6,2))

print("u can take transpose of an array with T method")
print(a.T)

print("resize makes the same thing but changes the original array "
)
a.resize(2, 6)
print(a)
print("it seems its deprecated why havent they removed it yet?")

print("when using reshape if u give -1 to one dimension" \
" it will be calculated automatically")
print(a.reshape(3, -1)) # 3 rows and 2 columns

a = np.floor(10 * rg.random((2, 2))) # turn to the start 
print(a)
b = np.floor(10 * rg.random((2, 2)))
print(b)
c = np.vstack((a, b)) # vstack = vertical stack alt alta ekle
print(c)

c = np.hstack((a, b)) # hstack = horizontal stack yan yana ekle 
print(c)

# The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to hstack only for 2D arrays:
# search in the website then continue https://numpy.org/devdocs/user/quickstart.html


print("next method is column_stack it takes 1D arrays and stacks them as columns" \
" into a 2D array. It is equivalent to hstack only for 2D arrays")

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(np.column_stack((a, b)))

print("the reason of the above is if u use 2D arrays")
first_array = [[9., 7., 1., 9.],
       [5., 2., 5., 1.]]
print(np.array(first_array)
      )
first_array = np.array(first_array)
second_array = [[1., 2., 3., 4.],
       [5., 6., 7., 8.]]
print(np.array(second_array))
second_array = np.array(second_array)

print("now if we use column stack")
print(np.column_stack((first_array, second_array)))
print("and hstack")
print(np.hstack((first_array, second_array))) # it's the same 



one_d_array = np.array([1, 2, 3, 4])
print("one dimensional array : ", one_d_array)
print(one_d_array.shape)
one_d_array = one_d_array[:, np.newaxis] # newaxis is used to increase the dimension of the existing array by one more dimension, when used once.
print("one dimensional array after using newaxis : ", one_d_array)
print(one_d_array.shape)
print("lets try to add a new axis to the 2D array")
one_d_array = one_d_array[:, np.newaxis] # dont do it it
print(one_d_array)
print(one_d_array.shape)

print("we make to union now its time to slice")

print("first method is hsplit it takes an" \
" array and how many parts u want to split it into")

long_array = np.floor(10 * rg.random((2, 12)))
print(long_array)
split_arrays = np.hsplit(long_array, 3) # split into 3 parts
for small_array in split_arrays:
    print(small_array)



print("u can specify the indices where u wanna split it starts from 1")


specific_split_arrays = np.hsplit(long_array, (2, 3,5)) # split into 3 parts but the second part is only 1 column
for small_array in specific_split_arrays:
    print(small_array)

print("vsplit is the same as hsplit but it splits vertically")
print(long_array)

split_arrays = np.vsplit(long_array, 2) # split into 2 parts
for small_array in split_arrays:
    print("**"*10)
    print(small_array)
    print("**"*10)
