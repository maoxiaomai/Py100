# coding: utf-8
# 计算字符串中子串出现的次数
# str1.count(str2)   ---str2在str1中出现的次数

long_str = input('input a long string: ')
short_str = input('input a short string: ')
a = long_str[:]

count = 0
result = long_str.find(short_str)
if result == -1:
    print(count)
else:
    count = 1
    while result != -1:
        long_str = long_str[result+len(short_str):]
        result = long_str.find(short_str)
        if result != -1:
            count += 1
    print(count)

count1 = a.count(short_str)
print(count1)