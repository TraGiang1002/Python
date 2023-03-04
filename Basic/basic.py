# If
code = 230
if code == 229:
    print('Hello CS229!')
elif code == 230:
    print('That\'s deep learning!')
elif code < 200:
    print('That is some undergraduate class')
else:
    print('Wrong class!')

true = True
false = False
if true:
    print("It's true!")
if not false:
    print("It's still true!")
if true and not false:
    print("Anyhow, it's true!")
if false or not true:
    print("True?")
else:
    print("Okay, it's false now....")

print(5/2)
print(5%2)
print(5**2)
print(5//2)

#Loop
for i in range(5):
    print(i)
a = 5
while a > 0:
    print(a)
    a-=1

#Function
def power(v, p=2):
    return v**p
print(power(10))
print(power(10, 3))

#đối số bổ sung
def func2(*args, **kwargs):
    print(args) #bến số của đối số không có từ khóa
    print(kwargs) #biên số của dối số có từ khóa

def func1(v, *args, **kwargs):
    func2(*args, **kwargs)
    if 'power' in kwargs:
        return v**kwargs['power']
    else:
        return v
print(func1(10, 'extra 1', 'extra 2', power=3))
print('-----------------')
print(func1(10, 5))

