# -*- coding: utf-8 -*-
# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 因子：因子就是所有可以整除这个数的数,不包括这个数自身。15的因子是1，3，5。28的因子：1，2，4，7，14
import math

for num in range(1, 1001):
    s = []
    for k in range(1, int(num/2)+1):
        if num % k == 0:
            s.append(k)
    if num == sum(s):
        print(num)
        a = ''
        for i in range(0, len(s)):
            a += str(s[i]) + '+'
            if i == len(s)-2:
                break
        a += str(s[-1])
        print(str(num)+"="+a)