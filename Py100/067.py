# coding: utf-8
# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

list = [1,2,3,7,9,8]
# print(list)
min = min(list)
max = max(list)
print(min,max)

for i in range(0, len(list)):
    if list[i] == max:
        list[i], list[0] = list[0], list[i]
        break

for j in range(0, len(list)):
    if list[j] == min:
        list[j], list[-1] = list[-1], list[j]
        break

print(list)