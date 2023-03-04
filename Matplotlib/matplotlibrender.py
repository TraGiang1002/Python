import matplotlib.pyplot as plt
import numpy as np

def draw_simple_sin_cos(x_values):
    y1_values = np.sin(x_values * np.pi)
    y2_values = np.cos(x_values * np.pi)
    # vẽ đồ thị
    plt.plot(x_values, y1_values, label='Sine')
    plt.plot(x_values, y2_values, label='Cosine')
    # vẽ chú thích
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('values')
    plt.title('Values for sin and cos, scaled by $\phi_i$')

x_values = np.arange(0, 20, 0.001) #mảng numpy chứa các giá trị từ 0 đến 20, với bước nhảy là 0.001

draw_simple_sin_cos(x_values)
plt.show()
#figsize: kích thước, dpi: độ phân giải
plt.figure(figsize=(10,3), dpi=100) # 640 x 450
draw_simple_sin_cos(x_values)

plt.savefig('tutorial_sin.jpg') #lưu đồ thị thành file ảnh jpg
plt.show()


def draw_subplot_sin_cos(index, x_values, ax):
    y1_values = np.sin(x_values * np.pi)
    y2_values = np.cos(x_values * np.pi)

    ax.plot(x_values, y1_values, c='r', label='Sine')
    ax.scatter(x_values, y2_values, s=4, label='Cosine')

    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('values')
    ax.set_title(f'Values for sin and cos (Subplot #{index})')
# lưới đồ thị gồm 2 hàng và 2 cột, tổng cộng 4 đồ thị, và lưu vào biến fig
#  mảng ax_list chứa các đối tượng tương ứng với từng ô trong lưới đồ thị.
fig, ax_list = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
#fig, ax_list = plt.subplots(nrows=2, ncols=2,
#                            sharex='col', sharey='row',
#                            figsize=(10, 10))
#
i = 0
# ax chính là một trong số các đối tượng AxesSubplot trong mảng ax_list
for r, row in enumerate(ax_list): # lấy lần lượt từng hàng ax_list
    for c, ax in enumerate(row): # lấy trong mỗi hàng ax thuộc chỉ số côt
        x_values = np.arange(i, i + 10, 0.1)
        draw_subplot_sin_cos(i, x_values, ax)
        i += 1

plt.show()

fig, ax = plt.subplots(figsize=(10,10))
color='YlGn'
labels = ['Python', 'C++', 'Fortran']
cm = np.array([[0.7, 0.3, 0.2], [0.1, 0.5, 0.4], [0.05, 0.1, 0.85]])

heatmap = ax.pcolor(cm, cmap=color) #vẽ heatmap trên ax với các giá trị trong cm.
fig.colorbar(heatmap) #thêm thanh màu bên cạnh heatmap
ax.invert_yaxis() #đảo ngược trục y
ax.xaxis.tick_top() #đưa các tick của trục x lên phía trên của heatmap

ax.set_title('Confusion Matrix')
ax.set_xlabel('Prediction')
ax.set_ylabel('Groud Truth')

ax.set_xticks(np.arange(cm.shape[0]) + 0.5, minor=False)
ax.set_yticks(np.arange(cm.shape[1]) + 0.5, minor=False)
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)
plt.show()

img_arr = np.random.random((256, 256))# 0 -> 1
print(img_arr.shape)
# vmin và vmax được sử dụng để chỉ định giá trị tối thiểu và giá trị tối đa của bản đồ màu
plt.imshow(img_arr, cmap='gray', vmin=0.2, vmax=0.25)
plt.show()
# Mỗi pixel của ảnh sẽ có giá trị được xác định bởi 3 giá trị trong khoảng từ 0 đến 1, tương ứng với độ sáng của các kênh màu đỏ, xanh lá cây và xanh dương.
img_arr = np.random.random((256, 256, 3))# R, C, (RGB)
print(img_arr.shape)
plt.imshow(img_arr, vmin=0, vmax=1)
plt.show()

img_arr = np.random.random((3, 256, 256))# (RGB) R C
print(img_arr.shape)
# thay đổi vị trí của các chiều trong ma trận 3 chiều img_arr từ (256, 256, 3) thành (256, 3, 256)
img_arr = np.moveaxis(img_arr, 0, -1)
print(img_arr.shape)
plt.imshow(img_arr, vmin=0, vmax=1)
plt.show()

import imageio
fname = 'sample.jpg'
img = imageio.v2.imread(fname)

print(img.shape)
plt.figure(dpi=250)   # dpi=500 -> larger
plt.imshow(img, vmin=0, vmax=10000, interpolation='bilinear')
plt.show()