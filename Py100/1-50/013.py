# -*- coding: utf-8 -*-
# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

import math
from sys import stdout

def factors(n):
    num = n
    a = ''
    k = 2
    flag = 0

    while flag == 0:
        isPrime = True
        for j in range(2, int(math.sqrt(num))+1):
            if num % j == 0:
                isPrime = False
                k = j
                break
        if isPrime == False:
            num = num // k
            a += str(k)+'*'
        else:  # 是质数时 或 Num=1时
            a += str(num)
            flag = 1

    print(str(n)+"=" +a)

factors(99)



def factors2(num):
    isPrime = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0 and num != i:
            isPrime = False
            num = num // i
            L.append(str(i)+'*')
            factors2(num)
            break
    if isPrime == True:
        L.append(str(num))

L=[]
n = 99
factors2(n)
a = ''
print(L)
for i in L:
    a += str(i)

print(str(n)+"=" +a)