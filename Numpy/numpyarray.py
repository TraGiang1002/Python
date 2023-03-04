import numpy as np
import pprint as pp

from_list = np.array([1, 2, 3])
pp.pprint(from_list)
print(f'\t Data type of integer is {from_list.dtype}')
from_list_2d = np.array([[1, 2, 3.0], [4, 5, 6]])
pp.pprint(from_list_2d)
print(f'\t Data type of float is {from_list_2d.dtype}')
from_list_bad_type = np.array([1, 2, 3, 'a'])
pp.pprint(from_list_bad_type)
print(np.ones(3)) # mảng 3 ptu = 1
print(np.ones((3, 3))) # ma trận 3x3 ptu=1
print(np.zeros(3)) # mảng 3 ptu = 0
print(np.zeros((3, 3))) # ma trận 3x3 ptu=0
print(np.eye(3)) # ma trận bậc thang 3x3 các ptu dường chéo chính = 1
print(np.random.random(3)) # mảng 3 ptu random
print(np.random.random((2, 2))) # ma trận 2x2 các ptu random
print(np.random.randn(3, 3)) # ma trận 3x3 các ptu random -1->1

#array shape
array_1d = np.array([1, 2, 3, 4])
array_1by4 = np.array([[1, 2, 3, 4]])
array_2by4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(array_1d.shape)# mảng 1 chiều 4 ptu
print(array_1by4.shape)# ma trận 1x4
print(array_2by4.shape)# ma trận 2x4
print(array_1d.reshape(-1, 4).shape) #thay đổi kích thước của mảng trên thành một ma trận có số dòng (rows) không xác định (-1) và số cột (columns) là 4.
print(array_2by4.size) # projects: pytorch -- size similar to numpy shape

large_array = np.array([i for i in range(400)])
large_array = large_array.reshape((20, 20)) #thay đổi kích thước của mảng trên thành một ma trận có 20x20
print(large_array[:, 5]) #lấy ra tất cả các phần tử ở cột thứ 5 của ma trận.

large_3d_array = np.array([i for i in range(1000)])
large_3d_array = large_3d_array.reshape((10, 10, 10))
print(large_3d_array[:, 1, 1])
print(large_3d_array[2, :, 1])
print(large_3d_array[2, 3, :])
print(large_3d_array[1, :, :])

small_array = np.arange(4)
print(np.reshape(small_array, (2, 2), order='C')) # Default order
print(np.reshape(small_array, (2, 2), order='F')) #thứ tự Fortran-style ordering

#numpy math
array_1 = np.array([1, 2, 3, 4])

# element wise operations!!
print(array_1 + 5)
print(array_1 * 5)
print(np.sqrt(array_1))
print(np.power(array_1, 2)) # mũ 2 các ptu
print(np.exp(array_1))
print(np.log(array_1))

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pp.pprint(array_2d)
print(f'shape={array_2d.shape}')
print(np.sum(array_2d))
print(np.sum(array_2d, axis=0))# cộng theo cột
print(np.sum(array_2d, axis=1))# cộng theo hàng

array_3d = np.array([i for i in range(8)]).reshape((2, 2, 2))
pp.pprint(array_3d)
print(np.sum(array_3d, axis=0))
print(np.sum(array_3d, axis=1))
print(np.sum(array_3d, axis=2))
print(np.sum(array_3d, axis=(1, 2)))

array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([3, 4, 5, 6])
print(array_1 * array_2) # element wise multiplication
# same as np.multiply
print(np.multiply(array_1, array_2))
print(array_2.reshape(4, -1))
print(array_2.shape)
print(array_2.reshape(4, -1).shape)
print(array_1 * array_2.reshape(4, -1)) # Come back to this later
# element wise multiplication --> sum
print(np.sum(array_1 * array_2))
print(array_1.dot(array_2))
print(np.dot(array_1, array_2))
print(array_1 @ array_2) # equivavlent to np.matmul(array_1, array_2)
print(array_1.shape)

array_1 = np.array([[1, 2, 3, 4]])
array_2 = np.array([[3, 4, 5, 6]])
print(array_1.shape)
print(array_2.shape)
print(array_1 * array_2)
# print(array_1.dot(array_2)) #error

# T for transpose
print(array_1.dot(array_2.T)) # inner product
print(array_1.T.dot(array_2)) # outer product
print(np.matmul(array_1, array_2.T)) # inner product
print(np.matmul(array_1.T, array_2)) # outer product
weight_matrix = np.array([1, 2, 3, 4]).reshape(2, 2)
sample = np.array([[50, 60]]).T
np.matmul(weight_matrix, sample)
# sanity check
print(weight_matrix.shape)
print(sample.shape)
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
print(np.matmul(mat1, mat2))
a = np.array([i for i in range(10)]).reshape(2, 5)
print(a * a)
print(np.multiply(a, a))
print(np.multiply(a, 10))