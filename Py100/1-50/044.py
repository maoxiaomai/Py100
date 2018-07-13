# coding: utf-8
# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

import numpy as np
# https://www.cnblogs.com/xzcfightingup/p/7598293.html

X = []
X.append([12,7,3])
X.append([4,5,6])
X.append([7,8,9])

Y = []
Y.append([5,8,1])
Y.append([6,7,3])
Y.append([4,5,9])

Z = [[0 for i in range(3)] for j in range(3)]
# print(X,Y)

for i in range(3):
    for j in range(3):
        Z[i][j] = X[i][j] + Y[i][j]
print(Z)
for z in Z:
    print(z)


# using numpy module
a = np.array([[12,7,3], [4,5,6], [7,8,9]])
b = np.array([[5,8,1], [6,7,3], [4,5,9]])
print(a+b)