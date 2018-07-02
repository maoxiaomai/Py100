# -*- coding: utf-8 -*-
# 题目：对10个数进行排序。

L = []
for i in range(0, 10):
    num = int(input("input a number: "))
    L.append(num)

print(L)
# L.sort()
# for i in L:
#     print(i, end=' ')

# 冒泡排序

for i in range(0, len(L)):
    for j in range(i+1, len(L)):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
print(L)