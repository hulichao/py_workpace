from functools import reduce
# map接受一个参数的抽象编程方法

# reduce接受两个参数的迭代计算

def fn(x,y):
    return x * 10 + y

def char2num(c):
    dis = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return dis[c]

def str2int(s):
    return reduce(fn, map(char2num, s))

print(str2int("234234"))


## filter

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['hello','  ', "X X",None,'A','B'])))


# sorted

print(list(sorted([36, 5, -12, 9, -21],key=abs,reverse=True)))

# 先按名字后按分数
stus = [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
sorted(stu, key=my_sort)




