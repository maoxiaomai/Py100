# coding: utf-8
# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

# list = [1,4,6,9,13,16,19,28,40,100]
list = [10,8,6,5,4,3,2,1]
num = int(input("input a number: "))
flag = 0

for i in range(0, len(list)):
    if list[0] < list[1]:
        if num <= list[i]:
            list.insert(i, num)
            flag = 1
            break
    else:
        if num >= list[i]:
            list.insert(i, num)
            flag = 1
            break
if flag == 0:
    list.append(num)

print(list)