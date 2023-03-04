import numpy as np
import pprint as pp

op1 = np.array([i for i in range(9)]).reshape(3, 3)
op2 = np.array([[1, 2, 3]])
op3 = np.array([1, 2, 3])

pp.pprint(op1)
pp.pprint(op2)
# Notice that the result here is DIFFERENT!
print(op1.shape)
print(op2.shape)
print(op2.T.shape)
pp.pprint(op1 + op2)
pp.pprint(op1 + op2.T)
# Notice that the result here are THE SAME!
print(op3.shape)
print(op3.T.shape)
pp.pprint(op1 + op3)
pp.pprint(op1 + op3.T)

op1 = np.array([i for i in range(225)]).reshape(15, 3, 5)
op2 = np.array([[1, 2, 3]])

# This does not work
# print(op1 + op2) #broadcast không thực hiện được giữa hai ma trận có kích thước khác nhau

# This works
print(op2.shape)
print(op2.T.shape)
print(op1.shape)
print(op1 + op2.T)

# BTW you can contract the cells by clicking on the left
array = np.array([1, 2, 3])
# np.tile(array, shape)
print(np.tile(array, 2))
print(np.tile(array, (2, 3)))

op1 = np.array([i for i in range(225)]).reshape(15, 3, 5)
op2 = np.array([[1, 2, 3]])
op_tiled= np.tile(op2, (1, 5))
# print(op1)
# print(op2.T)
print(op_tiled.shape)
op_tiled= np.tile(op2.T, (1, 5))
print(op_tiled)
print(op_tiled.shape)
#op_expanded sẽ trở thành một mảng ba chiều kích thước (1, 3, 1), với chiều thứ ba được thêm vào từ axis=2
op_expanded = np.expand_dims(op2, axis=2)
print(op_expanded)
print(op_expanded.shape)
op_tiled_2 = np.tile(op_expanded, (15, 1, 5))
print(op_tiled_2)
print(op_tiled_2.shape)

op3 = np.array([i for i in range(9)]).reshape(3, 3)
op_na = op3[np.newaxis, :]
print(op_na)
print(op_na.shape)

op_na2 = op3[:, np.newaxis, :]
print(op_na2)
print(op_na2.shape)

print(op_expanded)
print(op_expanded.shape)

op_squeezed = np.squeeze(op_expanded)
print(op_squeezed)

samples = np.random.random((15, 5))
print(samples.shape)
print(samples)

# Without broadcasting
expanded1 = np.expand_dims(samples, axis=1)
tile1 = np.tile(expanded1, (1, samples.shape[0], 1))
#print(expanded1.shape)
#print(tile1.shape)
#print(tile1)

expanded2 = np.expand_dims(samples, axis=0)
tile2 = np.tile(expanded2, (samples.shape[0], 1 ,1))
#print(expanded2.shape)
#print(tile2.shape)
#print(tile2)

diff = tile2 - tile1
distances = np.linalg.norm(diff, axis=-1)
# print(distances)
print(np.mean(distances))
# With scipy
import scipy.spatial
distances = scipy.spatial.distance.cdist(samples, samples)
# print(distances)
# print(len(distances))
print(np.mean(distances))