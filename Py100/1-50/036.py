# -*- coding: utf-8 -*-
# 求100之内的素数。
import math

for num in range(1, 101):
    isPrime = True
    if num == 1:
        pass
    elif num == 2:
        print(num, end=' ')
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                isPrime = False
                break
        if isPrime == True:
            print(num, end=' ')