# -*- coding: utf-8 -*-
# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

height = 100.0
# s = height
# for i in range(1,10):
#
#     height = height / 2  # 第i次反弹的高度
#     s += height * 2      # 第i+1落地经过的路程
#
# print("第10次落地经过%f米" % s)
# print("第10次反弹%f米" % (height/2))

s = 0

for i in range(1, 11):
    if i == 1:
        s = height   # 第1次落地
    else:
        s += height*2  # 第i次落地（i>=2）

    height /= 2     # 第i次弹起

print("第10次落地经过%f米" % s)
print("第10次反弹%f米" % height)