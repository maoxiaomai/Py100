# -*- coding: utf-8 -*-
# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。

s = []
for num in range(1, 21):
    res = 1
    for i in range(num, 0, -1):
        res = res * i
    s.append(res)

print(s)
print(sum(s))

def op(num):
    res = 1
    for i in range(num, 0, -1):
        res = res * i
    return  res

k = map(op, range(1, 21))
print(sum(k))