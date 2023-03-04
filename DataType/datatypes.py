#String
# https://docs.python.org/3/library/string.html
cs_class_code = 229
print('I like CS ' + str(cs_class_code) + ' a lot!')
print(f'I like CS {cs_class_code} a lot!')

print('I love CS229. (upper)'.upper()) #chữ in
print('I love CS229. (lower)'.lower()) #chữ thường
print('I love CS229. (rjust 50)'.rjust(50))
print('we love CS229. (capitalize)'.capitalize())
print('       I love CS229. (strip)        '.strip()) # loại bỏ khoảng thừa

print(f'{print} (print a function)')
print(f'{type(229)} (print a type)')

print('Old school formatting: {2}, {1}, {0:10.2F}'.format(1.358, 'b', 'c'))
# Fill in order of 2, 1, 0. For the decimal number, fix at length of 10, round to 2 decimal places

#List
# https://docs.python.org/3/tutorial/datastructures.html
list_1 = ['one', 'two', 'three']
list_2 = [1, 2, 3]
print(list_1)
print(list_2)
list_2.append(4) #Thêm 4 vào list_2
print(list_2)
list_2.insert(0, 'ZERO') #thay 0 trong list 2 thành ZERO
print(list_2) # if you go back to the previous cell and run print(list_2) again, what will you see?

print(list_1 + list_2)
list_1_temp = ['a', 'b']
list_1_temp.extend(list_2)#list_1_temp gộp với list_2
print(list_1_temp)

print(list_1 * 3 + list_2)
print([list_1] * 3 + list_2)

import pprint as pp
pp.pprint([list_1] * 5 + list_2)
pp.pprint([list_1] * 2 + [list_2] * 3)

long_list = [i for i in range(9)]
long_long_list = [(i, j) for i in range(3) for j in range(5)]
long_list_list = [[i for i in range(3)] for _ in range(5)]
pp.pprint(long_list)
pp.pprint(long_long_list)
pp.pprint(long_list_list)

string_list = ['a', 'b', 'c']
for s in string_list:
    print(s)
for i, s in enumerate(string_list):
    print(f'{i}, {s}')

print(long_list[:5])
print(long_list[:-1])
print(long_list[4:-1])
long_list[3:5] = [-1, -2]# thay ptu thứ 3 là -1, 4 là -2
print(long_list)
long_list.pop()#lấy ra ptu cuối cùng
print(long_list)

# https://docs.python.org/3/howto/sorting.html
random_list = [3, 12, 5, 6, 8, 2]
print(sorted(random_list))# sắp xếp nhỏ -> lớn
random_list_2 = [(3, 'z'), (12, 'r'), (5, 'a'), (6, 'e'), (8, 'c'), (2, 'g')]
print(sorted(random_list_2, key=lambda x: x[1])) # sắp xếp nhỏ -> lớn theo chỉ số 1
orig_list = [[1, 2], [3, 4]]
dup_list = orig_list #list là kiểu tham tri
dup_list[0][1] = 'okay'
pp.pprint(orig_list)
pp.pprint(dup_list)
a = [[1, 2, 3]]*3
b = [[1, 2, 3] for i in range(3)]
a[0][1] = 4 #đổi trước lặp sau
b[0][1] = 4 #lặp trước dổi sau
print(a)
print(b)

# https://docs.python.org/3/library/copy.html
import copy
orig_list = [[1, 2], [3, 4]]
dup_list = copy.deepcopy(orig_list)#copy chuyển list thành kiểu tham chiếu
dup_list[0][1] = 'okay'
pp.pprint(orig_list)
pp.pprint(dup_list)

# Tuple
my_tuple = (10, 20, 30)
# my_tuple[0] = 40 #error
a, b, c = my_tuple
print(f"a={a}, b={b}, c={c}")
for obj in enumerate(my_tuple):
    print(obj)

#Dictionary/Set
# https://docs.python.org/3/tutorial/datastructures.html
my_set = {i ** 2 for i in range(10)}
print(my_set)
my_set_temp = {i ** 2 % 5 for i in range(10)}
print(my_set_temp)
my_dict = {(5 - i): i ** 2 for i in range(10)}
print(my_dict)
print(my_dict.keys())
second_dict = {'a': 10, 'b': 11}
my_dict.update(second_dict)# thêm second_dict vào my_dict
pp.pprint(my_dict)
my_dict['new'] = 10 #thêm 'new': 10 vào my_dict
pp.pprint(my_dict)
for k, it in my_dict.items(): # similar to for loop over enumerate(list)
    print(k, it)
# Sorting keys by string order
for k, it in sorted(my_dict.items(), key=lambda x: str(x[0])):#săp xếp từ nhỏ đến lớn theo keys
    print(k, it)
# https://docs.python.org/3/library/collections.html