# -*- coding: utf-8 -*-
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

# num = int(input("请输入一个五位数： "))
# l = []
# while num != 0:
#     a = num % 10
#     l.append(a)
#     num = num // 10
#
# if l[0] == l[-1] and l[1] == l[-2]:
#     print("是回文数")
# else:
#     print("不是回文数")

num = input("请输入一个五位数： ")
flag = True

for i in range(0, len(num)//2):
    if num[i] != num[len(num)-i-1]:
        flag = False
        break
if flag == True:
    print(num + "是回文数")
else:
    print(num + "不是回文数")