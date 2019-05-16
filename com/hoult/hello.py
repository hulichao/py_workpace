# -*- coding: utf-8 -*-
# print("hello world2")
classmate=["army","kubo","strong"]
# print (classmate[0])
classmate.append("hoult")
classmate.insert(1, "john")
classmate.insert(2, "booy")
classmate.pop()
classmate[2] = "girl"
classmate.insert(1, 123)
classmate.insert(0, [True, False])
classmate.insert(0, classmate)
# print(classmate[0])
# print(classmate)

if 1 >= 0:
    print("hello")
elif 2 >= 3:
    print("no hello")

if 1:
    print("shadiao")

# birth = input("input your birth ")
# birth = int(birth)

birth = 10
if birth > 2000:
    print("00后")
else:
    print("90 hou")

sum = 0
for i in [1,2,3]:
    sum += i
print(sum)

sum = 0
for i in range(3):
    # print(i)
    sum += i
print(sum)

d = {'boy': 1, 'girl': 2}
d['stu'] = 10
print('stu' in d)

print(d.get('stu'))

print(d)

s = set([1,2,3])
s2 = set([2,3,4])

s2.remove(2)
print(s2)
print(s & s2)
print(s | s2)

a = list([2,1,3])
a.sort()
print(a)

def my_abs(x):
    if x >= 0:
        return -x
    else:
        return -x

print(abs(33))

if __name__ == '__main__':
    pass