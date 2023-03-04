import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv') # đọc file train.csv lưu vào data
data_short = data[:20] # lấy 20 dòng đầu của data lưu vào data_short
# print(data_short)
print(data['x_1'].describe())     # mô tả thuộc tính x_1 của data
data.describe()            # mô tả data
data_short.to_csv('data_short.csv', index=False)# lưu data_short vào file csv cùng tên
data_short[['x_1', 'y']]
data_short[(data_short['y'] > 5) & (data_short['x_3'] < 1.5)]       # Use & | instead of and/or. Put brackets around

def filter_func(row):
    if row['x_1'] == 1.0 and row['x_2'] == 0.0:
        return row['y'] * 10
    return -1
# Hàm này sẽ tạo một cột mới trong dataframe với tên là new_column được tính bằng cách áp dụng hàm filter_func lên mỗi dòng.
data_short['new_column'] = data_short[['x_1', 'x_2', 'y']].apply(filter_func, axis=1)
# print(data_short)

col2 = []
for i, row in data_short.iterrows():
    print(f'Row {i}: y-value: {row["y"]}')
    col2.append(row['y'] ** 2)

data_short['col_2'] = col2
print(data_short)
print(data.loc[19])
print(data.iloc[-1])

data_list = [{'a': i, 'b': i + 1} for i in range(15)]
data_list[5] = {'a': 10, 'b': 9, 'c': -1}

df = pd.DataFrame(data_list)
# print(df)
data_2d = np.array([i for i in range(50)]).reshape(5, 10)
df = pd.DataFrame(data_2d, columns=[f'col {i}' for i in range(10)], index=[f'row {i}' for i in range(5)])
# print(df)

data_dict = {'col 1': [3, 2, 1, 0], 'col 2': ['a', 'b', 'c', 'd']}

df = pd.DataFrame.from_dict(data_dict)
# print(df)
df = pd.DataFrame.from_dict(data_dict, orient='index')
# print(df)

data.plot(kind='scatter', x='x_3', y='y', title='Plot of Data');
plt.show()
data['y'].plot(kind='hist', title='Y');
plt.show()
data.boxplot(column='x_3', by='y');
plt.show()
data.to_numpy()
plt.show()
plt.scatter(data['x_1'], data['y'])
plt.show()