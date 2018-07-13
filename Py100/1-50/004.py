# -*- coding: UTF-8 -*-
#例4:输入某月某日，判断这一天是一年的第几天？

year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))

d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#d2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = False
sums = 0
if 0 < month <=12:
    # for i in range(0, month - 1):
    #     sum = sum + d[i]
    sums = sum(d[0:month-1])
    sums = sums + day
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    if leap == True and month > 2:
        sum += 1

    print("It is the %dth day" % sums)
else:
    print("Wrong month!")



