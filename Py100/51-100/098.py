# coding: utf-8
# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

f = open('/Users/Jessica/Documents/python_work/Py100/test1.txt', 'w')
str = input('input a string: ')
f.write(str.upper())

f.close()