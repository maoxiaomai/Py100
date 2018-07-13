# -*- coding: utf-8 -*-
# 题目：按相反的顺序输出列表的值。



s=['a','bbb','cc','dddd','e','ff']
# for i in range(0, len(s)):
#     print(s[len(s)-i-1])
s.reverse()     # list.reverse() 该方法没有返回值，但是会对列表的元素进行反向排序。
for j in s:
    print(j)