# -*- coding: utf-8 -*-
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
L=[]
for i in range(0,3):
    x = int(input("input a number: "))
    L.append(x)
L.sort()
print(L[0],L[1],L[2])

# if x>y:
#     temp = x
#     x = y
#     y = temp
# if x>z:
#     temp = x
#     x = z
#     z = temp
# if y>z:
#     temp = y
#     y = z
#     z = temp
# print(x,y,z)


