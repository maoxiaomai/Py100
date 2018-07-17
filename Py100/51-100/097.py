# coding: utf-8
# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

f = open('/Users/Jessica/Documents/python_work/Py100/test.txt', 'w')
while True:
    a = input('input characters: ')
    if a == '#':
        break
    f.write(a)

f.close()