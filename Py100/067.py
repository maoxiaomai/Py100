# coding: utf-8
# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

list = [1,2,3,7,9,8]
sort_list = sorted(list)
# print(list)
# print(sort_list)
min = sort_list[0]
max = sort_list[-1]
print(min,max)
count = 0
for i in list:
    if i == max:
        count1 = count
        break
    count += 1
list[0], list[count1] = max, list[0]
#print(list)

count3 = 0
for i in list:
    if i == min:
        count2 = count3
        break
    count3 += 1
list[-1], list[count2] = min, list[-1]

print(list)