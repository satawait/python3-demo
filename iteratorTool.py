#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1, 2)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    nsN = itertools.takewhile(lambda x: x <= 2 * N - 1, natuals)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    cs = itertools.cycle([1, -1])
    # step 4: 求和:
    sum = 0   
    for i in nsN:
        sum += 4 * next(cs) / i
    return sum

print(pi(1000))