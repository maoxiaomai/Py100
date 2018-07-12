# coding: utf-8
# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

# 1 2 3 4 5 6 7 8
# 4 5 6 7 8 1 2 3

def move(n,m):  # n>m
    L= []
    for i in range(0, n):
        L.append(int(input("enter %dth number: " %(i+1))))
    print(L)
    M = []
    M[0:m] = L[(n-m):]
    M[m:n] = L[0:(n-m)]
    print(M)

move(8,5)