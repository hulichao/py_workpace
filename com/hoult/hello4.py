from collections import Iterable
import os
# 切片

L = list(range(100))

print(L[::2])

s = " sdfas "

print("前s",s)
while s[:1] == ' ':
    s = s[1:]
while s[-1:] == ' ':
    s = s[:-1]
print("后s",s)

d = {'a': 1, 'b': 2, 'c': 3}

for i in d.items():
    print(i)


# 迭代
print(isinstance("acca", Iterable))
print(isinstance([], Iterable))

for i,value in enumerate(L):
    print(i,"ss%s" %  value)

# 列表生成式

print([x*y for x in list(range(10)) for y in list(range(1,11))])

print([d for d in os.listdir('.')])

print(isinstance("", str))

# 斐波那契数列

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(a)
        yield b
        a, b = b, a + b
        n += 1
    return "good"

# print(next(fib(4)))

g = fib(6)

while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        print("迭代结束", e.value)
        break


