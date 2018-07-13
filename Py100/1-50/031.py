# -*- coding: utf-8 -*-
# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。

day = input("输入星期几： ")

if day[0].lower() == 's':
    if day[1].lower() == 'a':
        print("星期六")
    elif day[1].lower() == 'u':
        print("星期日")
elif day[0].lower() == 'm':
    print("星期一")
elif day[0].lower() == 't':
    if day[1].lower() == 'u':
        print("星期二")
    elif day[1].lower() == 'h':
        print("星期四")
elif day[0].lower() == 'w':
    print("星期三")
elif day[0].lower() == 'f':
    print("星期五")
else:
    print('wrong input')