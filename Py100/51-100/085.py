# coding: utf-8
# 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

num = int(input('Input a odd number: '))
a = 9
count = 1
while a % num != 0:
    a = a * 10 + 9
    count += 1
print('%d 个 9 可以被 %d 整除：%d'%(count, num, a))
print('%d / %d = %d'%(a, num, a/num))