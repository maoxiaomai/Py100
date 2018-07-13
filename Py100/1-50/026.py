# -*- coding: utf-8 -*-
# 题目：利用递归方法求5!。
# 程序分析：递归公式：fn=fn_1*4!


def cal(n):
    if n == 1:
        return 1
    else:
        s = n * cal(n-1)
        #print(s)
        return s

print(cal(5))