# -*- coding: UTF-8 -*-

# python装饰器分七步走

'''
1.用简单的函数，表示调用了两次
2.替换函数，利用装饰器
    装饰函数的参数是被装饰的函数对象，返回原函数对象
3.使用语法糖，注解。
'''


def deco(func):
    def _deco(*args, **kwargs):
        print("before myfunc() called.")
        ret = func(*args, **kwargs)
        print("  after myfunc() called. result: %s" % ret)
        return ret

    return _deco


@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b


myfunc(1, 2)
myfunc(3, 4)
