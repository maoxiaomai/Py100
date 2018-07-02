# -*- coding: utf-8 -*-
# 题目：对10个数进行排序。

L = []
for i in range(0, 10):
    num = int(input("input a number: "))
    L.append(num)

# print(L)
L.sort()
for i in L:
    print(i, end=' ')