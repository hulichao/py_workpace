# 面向对象


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


stu1 = Student("amy", 15)
stu2 = Student("john", 18)

stu1.print_score()
stu2.print_score()

a = 10
print(a)
a = "ss"
print(a)

print(stu1)

