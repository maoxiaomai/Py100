# -*- coding: utf-8 -*-
# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

# 1: a1           1
# 2: a2           1
# 3: A a1         2
# 4: A a2 a1      3
# 5: A A  a2 a1 a1   5
# 6: A A  A  a2 a2 a1 a1 a1  8
# 7: A A  A  A  A  a2 a2 a2 a1 a1 a1 a1 a1   13
# 8: A A  A  A  A  A  A  A  a2 a2 a2 a2 a2 a1 a1 a1 a1 a1 a1 a1 a1   21

def rabbit(n):
    a, b = 1, 1
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        for i in range(0,n-1):
            a, b = b, a+b
        return a

print(rabbit(8))



