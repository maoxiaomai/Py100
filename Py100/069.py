# coding: utf-8
# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

# 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32, 34
# 2  3  1  2  3  1  2   3   1   2   3   1   2   3   1   2   3   1   2   3   1   2   3
# 1,  4, 5, 8, 10, 13, 14,  17, 19,  22, 23,  26, 28, 31, 32       15
# 1   2  3  1  2   3   1    2   3    1   2    3   1   2   3
# 1,  4, 8, 10, 14,  17,  22, 23,  28, 31    10
# 1,  4, 10, 14,   22, 23,   31
# 1,   10, 14,    23,   31
# 10, 14,    31
# 10,  31
# 10

# 方法一：  不大好
# def last(n):
#     L = [i for i in range(1, n+1)]
#     k = 1
#     while len(L) > 1:
#         M = []
#         for j in range(k, len(L)+k):
#             if j % 3 != 0:
#                 M.append(L[j-k])
#         k = (len(L)+(k-1)) % 3 + 1
#         L[:] = M[:]
#         #print(L)
#
#     print(L)
#
# last(34)


# 方法二
def last1(n):
    L = [i for i in range(1, n + 1)]
    count = 0    # 设置一个变量，用于计算报数
    while len(L) > 1:  # 当只有一个数时才中止循环
        M = L[:]       # 把原数组拷贝到临时新数组中，用于限制内层循环次数
        for j in range(0, len(M)):   # 内层循环开始，从第一个人开始报数
            count += 1    # 每报一次，count计数器加1。新一次循环继续累加，实现头尾相接
            if count % 3 == 0:    # 如果count能被3整除，则是报到3的人，移除
                L.remove(M[j])    # 把报到3的人移除原数组，进行下一次循环
                # print(M)

        print(L)

    print(L)

last1(34)