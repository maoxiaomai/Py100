# coding: utf-8
# 求输入数字的平方，如果平方运算后小于 50 则退出。

while True:
    num = float(input("input number: "))
    print("%f^2 = %f" %(num, num**2))
    if num**2 < 50:
        break