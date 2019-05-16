#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 偏函数 这也是语法糖
import functools
int2 = functools.partial(int, base = 2)

print(int2("1001010010"))

## 模块的使用
