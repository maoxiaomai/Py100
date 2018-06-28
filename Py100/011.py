# -*- coding: utf-8 -*-
# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
import math

def prime(L):
    num = 0
    p = []
    for i in range(L[0], L[1]+1):
        isPrime = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            p.append(i)
            num += 1
    print("[%d, %d] has %d primes:" % (L[0], L[1], num))
    print(p)

prime([101,200])