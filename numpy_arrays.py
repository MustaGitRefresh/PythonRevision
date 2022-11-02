# there are two ways for importing the modules import numpy as np
# import numpy as np this can also be
from numpy import *

# Array using array function
"""This int mentioning is not necessary and if float is mention then whole array will convert to float elements of 
array. """


# array = array([numbers for numbers in range(10, 51, 10)], float
# array = array(['a', "b", "c", "d", "e", "f"])
# array1 = array  # This will create a new array as the initiated array or variable
# print(array)
# print(array1)
# creating the array using Line space function
# a = linspace(0, 10, 5)
# print(a)
# creating the array using logspace
# al = logspace(1, 4, 5)
# for i in range(len(al)):
#     print('%.1f ' % al[i], end='')
# creating the array using the arange function
# arange_arr = arange(2, 11, 2)
# print(arange_arr)
# creating the array using Zeros and Ones
# a_z = zeros(5, int)
# a_z_f = zeros(5)  # default will be float
# a_o = ones(5, int)
# a_o_f = ones(5)
# print(a_z)
# print(a_o)
# print(a_z_f)
# print(a_o_f)
# Mathematical operations on Arrays
# math_array = array([10, 20, 30.5, -40])
# print(f'Original array {math_array}')
# print(f'After adding {math_array+5}')
# print(f'After subtracting {math_array-5}')
# print(f'After dividing {math_array/5}')
# print(f'After multiplication {math_array*5}')
# print(f'After modulus {math_array%5}')
# print("After functions")
# print(f"Sin {sin(math_array)}")
# print(f"Tan {tan(math_array)}")
# print(f"Cos {cos(math_array)}")
# print(f"Max {max(math_array)}")
# print(f"Min {min(math_array)}")
# print(f"Sum {sum(math_array)}")
# print(f"Average {mean(math_array)}")
# Comparing Arrays
# a = array([1, 2, 3, 0])
# b = array([0, 2, 3, 1])
# c = a == b
# print(f'a==b {c}')
# c = a < b
# print(f'a < b {c}')
# c = a > b
# print(f'a < b {c}')
# # with any and all
# print(f'If any one is True: {any(c)}')
# print(f'If any one is True: {all(c)}')
# Logical _ or, and, not
# a = array([1, 2, 3])
# b = array([0, 2, 3])
# c = logical_and(a > 0, a < 4)
# print(c)
# c = logical_or(b >= 0, b == 1)
# print(c)
# c = logical_not(b)
# print(c)
# Where function in numpy
# a = array([10, 21, 30, 41, 50], int)
# c = where(a % 2 == 0, a, 0)
# print(c)
# a1 = arange(10, 60, 10)
# b1 = array([1, 21, 3, 40, 51])
# c1 = where(a1 > b1, a1, b1)
# print(c1)
# NonZeros function
# a2 = array([1, 2, 0, -1, 0, 6], int)
# c2 = nonzero(a2)
# for i in c2:
#     print(i)
# print(a2[c2])
# Aliasing Arrays
# a3 = arange(1, 6)
# b = a3
# print(f'Original array {a3}')
# print(f'Aliased array {b}')
# b[0] = 99
# print(a3)
# print(b)
# Viewing and copying arrays
# a4 = arange(1, 6)
# b = a4.view()
# print(f'Original array {a4}')
# print(f'Aliased array {b}')
# b[0] = 99
# print(a4)
# print(b)
# copying
# a5 = arange(1, 6)
# b = a5.copy()
# print(f'Original array {a5}')
# print(f'Aliased array {b}')
# b[0] = 99
# print(a5)
# print(b)
# Slicing and Indexing arrays
# slicing_array = arange(10, 16)
# print(slicing_array)
# b = slicing_array[1:6:2]
# print(b)
# b = slicing_array[::]
# print(b)
# b = slicing_array[-2:2:-1]
# print(b)
# b = slicing_array[:-2:]
# print(b)
# indexing and looping
# a = arange(10, 16)
# print(a)
# a = a[1:6:2]
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1
# Dimensions of arrays
# 1D, 2D and 3D and etc.
# arr1_d = array([1, 2, 3])
# arr2_d = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# arr3_d = array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [1, 1, 1],
#         [1, 0, 1]
#     ]
# ])
# print(arr1_d)
# print('\nNew')
# print(arr2_d)
# print('\nNew')
# print(arr3_d)
# Attributes of Arrays
# 1. ndim
# arr1_ndim = array([1, 2, 3, 4, 5])
# print(arr1_ndim.ndim)
# arr2_ndim = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr2_ndim.ndim)
# 2. shape
# arr1_shape = array([1, 2, 3, 4, 5])
# print(arr1_shape.shape)
# arr2_shape = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr2_shape.shape)
# # changing the shape of array
# arr2_shape.shape = (3, 2)
# print(arr2_shape)
# 3. Size
# arr1_size = array([1, 2, 3, 4, 5])
# print(arr1_size.size)
# arr2_shape = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr2_shape.shape)
# print(arr2_shape.size)
# 4. Item size
# arr1_itemsize = array([1, 2, 3, 4, 5])
# print(arr1_itemsize.itemsize)
# arr2_shape = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr2_shape.shape)
# print(arr2_shape.itemsize)
# 5. dtype
# arr1_dtype = array([1, 2, 3, 4, 5])
# print(arr1_dtype.dtype)
# arr2_shape = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr2_shape.shape)
# print(arr2_shape.dtype)
# 6. n bytes this gives the total bytes of the array consuming
#
#
# def n_bytes_custom(array_in):
#     array_in_itemsize = array_in.itemsize
#     array_in_size = array_in.size
#     n_bytes = array_in_size * array_in_itemsize
#     return n_bytes
#
#
# arr1_n_bytes = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr1_n_bytes.nbytes)
# print(n_bytes_custom(arr1_n_bytes))
# Methods
# 1. reshape()
# arr1_reshape = arange(10)
# arr1_reshape_1 = arr1_reshape.reshape(2, 5)
# arr1_reshape_2 = arr1_reshape.reshape(5, 2)
# print(arr1_reshape_1)
# print()
# print(arr1_reshape_2)
# 2. flatten()
# arr1_flatten = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr1_flatten)
# print(arr1_flatten.flatten())
# Multi-dimensional arrays creation and interaction
# 1. array
# arr1_array = array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ])
# print(arr1_array)
# print(arr1_array.nbytes*8)
# 2. Zeros and Ones
# ones
# arr1_ones = ones((3, 4), int)
# arr2_ones = ones((3, 4), float)
# print(arr1_ones)
# print(arr2_ones)
# print('The size of the array and their difference')
# print(arr1_ones.nbytes)
# zeros
# arr1_zeros = zeros((3, 4), int)
# arr2_zeros = zeros((3, 4), float)
# print(arr1_zeros)
# print(arr2_zeros)
# print('The size of the array and their difference')
# print(arr1_zeros.nbytes)
# print(arr2_zeros.nbytes)
# 3. eye
# arr1_eye = eye(5, dtype=int)
# print(arr1_eye)
# print(arr1_eye.nbytes)
# 4. reshape()
# arr1_reshape = array(
#     [1, 2, 3, 4, 5, 6]
# )
# b = reshape(arr1_reshape, (2, 3))
# print(b)
# c = reshape(arr1_reshape, (3, 2))
# print(c)
# arr2_reshape = arange(12)
# d = reshape(arr2_reshape, (2, 3, 2))
# e = reshape(arr2_reshape, (3, 2, 2))
# print(d)
# print(2)
# print(e)
# arr = arange(1, 11)
# print(arr)
# DF = pd.DataFrame(arr)
# DF.to_csv('data1.csv')
# Indexing the multi-dimensional array
# The error was occurring because of the
# a_m_d = arange(1, 9)
# d = reshape(a_m_d, (2, 4))
# for i in range(len(d)):
#     for j in range(len(d[i])):
#         print(d[i][j])
# indexing the 3D array
# arr3 = arange(1, 13)
# arr3 = reshape(arr3, (2, 3, 2))
# for i in range(len(arr3)):
#     for j in range(len(arr3[i])):
#         for k in range(len(arr3[i][j])):
#             print(arr3[i][j][k], end='\t')
#         print()
#     print()
# Slicing the multi-dimensional array
# a = array(
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
# )
# print(a[:, :])
# print()
# print(a[::])
# print()
# print(a[:])
# print(a[0:3, 0:2])
# a slicing program
# arr1_slice = reshape(arange(11, 36, 1), (5, 5))
# print(arr1_slice)
# print()
# print(arr1_slice[0:2, 0:3])
# print()
# print(arr1_slice[0:2, 2:])
# print()
# print(arr1_slice[2:, 3:])
# Matrices in numpy
# array to matrix
# a = array(
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
# )
# b = matrix(a)
# print(b)
# string to matrix
# a_str = """
#         1 2; 3 4; 5 6
#         """
# b_matrix = matrix(a_str)
# print(b_matrix)
# Getting the diagonals of the matrices
# a = matrix('1 2 3; 4 5 6; 7 8 9')
# print(a)
# d = diagonal(a)
# print(d)
# e = matrix('1 2 3; 4 5 6; 7 8 9')
# Finding the maximum and minimum
# print(e.min())
# print(e.max())
# Finding sum and average
# print(e.sum())
# print(e.mean())
# Finding the products of matrices 0 depicts column and 1 depicts rows
# array_matrix_product = matrix(arange(12).reshape(3, 4))
# print(f'The prod is \n{array_matrix_product.prod(0)}')
# print('New')
# print(f'The prod is \n{array_matrix_product.prod(1)}')
# Sorting the matrices
# array_matrix_sort = matrix(
#  [
#    [5, 4, 1],
#    [2, 7, 0]
#  ]
# )
# print(sort(array_matrix_sort, axis=0))
# print(sort(array_matrix_sort, axis=1))
# print(sort(array_matrix_sort.ravel()))
# Transpose of matrix
# m = matrix('1 2 3; 4 5 6; 7 8 9')
# print(m)
# print('After transposing')
# print(m.transpose())
# print('With getT')
# print(m.getT())
# Program for taking the array as input and giving the user the transposed version of the given array
# r, c = [int(a) for a in input("Enter the rows, cols: ").split()]
# values = input("Enter the matrix elements:\n")
# x = reshape(matrix(values), (r, c))
# print('The original matrix:\n')
# print(x.shape)
# print("Transpose array")
# y = x.transpose()
# print(y.shape)
# Matrix addition and Multiplication
# a = matrix('1 2 3; 4 5 6')
# b = matrix('2 2 2; 1 -1 2')
# print(a)
# print("new")
# print(b)
# print("new")
# c = a+b
# print(c)
# print("new")
# c = a/b
# print(c)
# print("new")
# c = a-b
# print(c)
# sum = 0
# for i in range(19, 30, 2):
#     sum += i
# print(sum)
# Random Numbers and arrays formation
# a = random.rand(2, 3)
# print(a)
