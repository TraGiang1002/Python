import numpy as np
from tqdm import tqdm
import time

a = np.random.random(500000)
b = np.random.random(500000)
p_tic = time.perf_counter()# thời gian CPU
tic = time.time()# thời gian thực
dot = 0.0;

for i in tqdm(range(len(a))):
    dot += a[i] * b[i]
print(dot)

toc = time.time()
p_toc = time.perf_counter()

print(f'Result: {dot}');
print(f'Compute time (wall): {round(1000 * (toc - tic), 6)}ms')
print(f'Compute time (cpu) : {round(1000 * (p_toc - p_tic), 6)}ms\n')

#####################################################################

p_tic = time.perf_counter()
tic = time.time()

print(np.array(a).dot(np.array(b))) # nhân 2 mảng bằng dot

toc = time.time()
p_toc = time.perf_counter()

print(f'(vectorized) Result: {dot}');
print(f'(vectorized) Compute time: {round(1000 * (toc - tic), 6)}ms')
print(f'(vectorized) Compute time (cpu) : {round(1000 * (p_toc - p_tic), 6)}ms')

def matrix_mul(X, Y):
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

X = np.random.random((200, 200))
Y = np.random.random((200, 200))
result = np.zeros((200, 200))

p_tic = time.perf_counter()
tic = time.time()

# iterate through rows of X
for i in tqdm(range(len(X))):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j] #tích 2 ma trận được lưu vào ma trận result
#  tổng các phần tử của ma trận result được tính bằng hàm np.sum() và lưu vào biến s.
s = np.sum(result)

toc = time.time()
p_toc = time.perf_counter()

print(f'Result: {s}');
print(f'Compute time (wall): {round(1000 * (toc - tic), 6)}ms')
print(f'Compute time (cpu) : {round(1000 * (p_toc - p_tic), 6)}ms\n')

#####################################################################

p_tic = time.perf_counter()
tic = time.time()

result = np.matmul(X, Y) #nhân 2 ma trận bằng matmul
s = np.sum(result)

toc = time.time()
p_toc = time.perf_counter()

print(f'(vectorized) Result: {s}');
print(f'(vectorized) Compute time: {round(1000 * (toc - tic), 6)}ms')
print(f'(vectorized) Compute time (cpu) : {round(1000 * (p_toc - p_tic), 6)}ms')

samples = np.random.random((100, 5))

p_tic = time.perf_counter()
tic = time.time()

total_dist = []
for s1 in samples:
    for s2 in samples:
        d = np.linalg.norm(s1 - s2) #tính toán norm (chuẩn) của vector s1 - s2, trong đó s1 và s2 là hai vector đầu vào.
        total_dist.append(d)

avg_dist = np.mean(total_dist)

toc = time.time()
p_toc = time.perf_counter()

print(f'Result: {avg_dist}');
print(f'Compute time (wall): {round(1000 * (toc - tic), 6)}ms')
print(f'Compute time (cpu) : {round(1000 * (p_toc - p_tic), 6)}ms\n')

#####################################################################

p_tic = time.perf_counter()
tic = time.time()
#tạo một mảng 3 chiều trong đó trục thứ nhất là các phần tử trong samples,
# trục thứ hai là các phần tử trong samples và trục thứ ba là tọa độ của mỗi phần tử trong samples.
diff = samples[:, np.newaxis, :] - samples[np.newaxis, :, :]
# print(diff)
# tính khoảng cách Euclide giữa mỗi cặp điểm trong samples
# bằng cách tính độ dài của vector khoảng cách diff trên trục thứ ba.
distances = np.linalg.norm(diff, axis=-1)
#tính trung bình của tất cả các khoảng cách.
avg_dist = np.mean(distances)

toc = time.time()
p_toc = time.perf_counter()

print(f'Result: {avg_dist}');
print(f'Compute time (wall): {round(1000 * (toc - tic), 6)}ms')
print(f'Compute time (cpu) : {round(1000 * (p_toc - p_tic), 6)}ms\n')

# np.show_config()