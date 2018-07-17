# coding: utf-8
# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

from sys import stdout

num = int(input('Input a 4-digit number: '))
d = num % 10
c = (num // 10) % 10
b = (num // 100) % 10
a = num // 1000
print(a,b,c,d)

a = (a + 5) % 10
b = (b + 5) % 10
c = (c + 5) % 10
d = (d + 5) % 10
a, d = d, a
b, c = c, b

print(a,b,c,d)
