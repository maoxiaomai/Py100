# -*- coding: utf-8 -*-
# 题目：按逗号分隔列表。

s = [1, 2, 3, 4, 5, 7, 8]
# print(s)
# L = []
#
# for i in range(0, len(s)):
#     L.append(s[i])
#     if i != len(s)-1:
#         L.append(',')
#
# for i in L:
#     print(i, end='')
s1 = ","
print (s1.join( map(str, s) ))


# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# str.join(sequence)
# sequence -- 要连接的元素序列。
# s1 = "-"
# s2 = ""
# seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
# print (s1.join( seq ))
# print (s2.join( seq ))

# 结果：
# r-u-n-o-o-b
# runoob