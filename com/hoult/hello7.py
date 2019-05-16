# -*- coding: utf-8 -*-
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print(fn.__name__ + "的执行时间",end - start)
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print("测试成功")

# 装饰器高级 @log @log('execute') 函数调用的前后打印出'begin call'和'end call'

def log(wrapper):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            start = time.time()
            result = fn(*args, **kw)
            end = time.time()
            print(fn.__name__ + "的执行时间", end - start)
            return result
        return wrapper
    return metric()

