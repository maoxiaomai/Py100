# coding: utf-8
# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

f1 = open('/Users/Jessica/Documents/python_work/Py100/test.txt', 'r')
out1 = f1.read()
f2 = open('/Users/Jessica/Documents/python_work/Py100/test1.txt', 'r')
out2 = f2.read()
print(out1)
print(out2)
new = out1 + out2
print(new.sorted())
