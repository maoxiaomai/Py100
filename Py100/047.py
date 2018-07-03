# coding: utf-8
# 两个变量值互换。

a = int(input("input a: "))
b = int(input("input b: "))
a, b = b, a

print(a, b)