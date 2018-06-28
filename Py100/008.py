# -*- coding: utf-8 -*-
# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

# for i in range(1,10):
#     out = ""
#     for j in range(1,10):
#         out += str(i) + "*" + str(j) + "=" +str(i*j) + " "
#         if i == j:
#             break
#     print(out)

for i in range(1,10):
    for j in range(1,10):
        print("%d*%d=%d\t" %(i, j, i*j), end='')  #print默认会换行。添加end=''不换行
        if i == j:
            print("") #换行
            break