# coding: utf-8
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

num = int(input('Input a number: '))


def f1(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += 1 / i
    print(sum)
def f2(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += 1 / i
    print(sum)

if num % 2 == 0:
    f1(num)
else:
    f2(num)