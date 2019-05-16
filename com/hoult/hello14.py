#  动态语音的鸭子特性，对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型
# 或者它的子类，否则，将无法调用run()方法。
#  对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：


class Animal(object):
    def run(self):
        print("animal is running")


class Cat(Animal):
    def run(self):
        print("cat is runnint")


class Dog(Animal):
    def run (self):
        print("dog is running")


def run_twice(animal):
    animal.run()
    animal.run()


class Time(object):
    def run(self):
        print("time is run")


a = Cat()
b = Dog()

run_twice(a)
run_twice(b)
run_twice(Time())


