# coding: utf-8
# 题目：求一个3*3矩阵主对角线元素之和。

a = []
sum = 0
for i in range(0, 3):
    a.append([])
    for j in range(0, 3):
        num = int(input("input a number: "))
        a[i].append(num)
        # if i == j:
        #     sum = sum + num
for i in range(0, 3):
    sum += a[i][i]

print(a)
print(sum)
# print(a[2][2])

# Python中初始化一个5 x 3每项为0的数组，最好方法是：
# multilist = [[0 for col in range(5)] for row in range(3)]

# 多维矩阵：
# https://www.cnblogs.com/xzcfightingup/p/7598293.html
# https://blog.csdn.net/chent86/article/details/76735262

# map = []
#
# for i in range(0, 5):
#   map += [[]]
#   for j in range(0, 3):
#     map[i] += [0]
#
# print(map)

# 简化：
# map = [[0 for i in range(5)] for i in range(3)]
# map(list)