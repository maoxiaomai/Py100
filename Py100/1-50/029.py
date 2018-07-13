# -*- coding: utf-8 -*-
# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

def num(n, s):
    if n == 0:
        return s
    else:
        a = n % 10
        s.append(a)
        num(n//10, s)
    #return s

n = int(input("input a number: "))
s = []
num(n, s)
print("The length of the number is %d" %len(s))
for d in s:
    print(d, end='')