# -*- coding: utf-8 -*-
# 题目：对10个数进行排序。

#L=[3, 55, 28, 91, 25, 87, 44]
# print(L)
# # L.sort()
# # for i in L:
# #     print(i, end=' ')
#
#
#
# count = 0
# for i in range(0, len(L)-1):
#     for j in range(i+1, len(L)):
#         if L[i] > L[j]:
#             L[i], L[j] = L[j], L[i]
#         count += 1
#     print(L)
# print(count)


# 冒泡排序
def bubble_sort(nums):
    #count = 0
    for i in range(0, len(nums)-1):
        for j in range(0, len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            count += 1
        print(nums)
    #print(count)
    return nums

nums=[3, 55, 28, 91, 25, 87, 44]
bubble_sort(nums)
