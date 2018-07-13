# coding: utf-8
# 题目：打印出杨辉三角形（要求打印出10行如下图）。

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1

def angles(num):
    a = []
    for i in range(0, num):
        if i == 0:
            print(1)
        else:
            L = []
            for j in range(0, i-1):
                L.append(a[j]+a[j+1])
            L.insert(0,1)
            L.append(1)
            for k in L:
                print(k, end=' ')
            print('')
            a = L[:]

angles(11)

# a = []
# for i in range(0, 10):
#     if i == 0:
#         for n in range(0, 10-i-1):
#             print('  ', end = '')
#         print(1)
#     else:
#         L = []
#         for j in range(0, i-1):
#             L.append(a[j]+a[j+1])
#         L.insert(0,1)
#         L.append(1)
#         for n in range(0, 10-i-1):
#             print('  ', end='')
#         for k in L:
#             print(k, end='   ')
#         print('')
#         a = L[:]