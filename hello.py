#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# print('中文测试正常')
# print('Hello %.2f' % 12.33333)
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs(-11.2))
# def findMinAndMax(L):
#     if len(L) == 0:
#        return (None, None)
#     max = L[0]
#     min = L[0]
#     for x in L:
#        min = x if x < min else min
#        max = x if x > max else max
#     print(min, max)
#     return (min, max)

# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!1')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!2')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!3')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!4')
# else:
#     print('测试成功!')
# name = 'gggass'
# a = (name[0]).upper()
# # name = a + name[1:].join('')
# print(''.join(name[1:]))
# a = [1, 2, 3, 4]
# a = filter(lambda x: x > 2, a)
# for i in a:
#     print(i)
# a = range(0, 10)
# for x in a:
#     print(x)
# f = open('./hello.txt', 'r')
# print(f.read())
# with open('./hello.txt', 'r', encoding='utf-8') as f:
#     for x in f.readlines():
#         print(x.strip())
# with open('./hello.txt', 'a', encoding='utf-8') as f:
#     f.write('\n好的')
# from io import StringIO
# f = StringIO('Hello\n你好\n好的')
# for line in f.readlines():
#     print(line.strip())
import pickle
import json

d = dict(name='jack', gender='male')
with open('./hello.txt', 'wb') as f:
    pickle.dump(d, f)
with open('./hello.txt', 'rb') as f:
    d = pickle.load(f)
    for i in d:
        print(i, d[i])

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))