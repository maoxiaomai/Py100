# coding: utf-8
# 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

for i in range(0, 7):
    num = int(input('Enter a number: '))
    # for j in range(0, num):
    #     print('*', end='')
    # print('')
    print(num*'*')