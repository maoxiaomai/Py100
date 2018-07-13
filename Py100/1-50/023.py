# -*- coding: utf-8 -*-
# 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 5 5 2
# 6 3 4
# 7 1 6   7-2*(i-4)=7-2*i+8=15-2*i


from sys import stdout

# for i in range(1, 8):
#     if i <= 4:
#         for j in range(1, 4-i+1):  # 空格
#             print(' ', end="")
#         for k in range(1, 2*i-1+1):  # *
#             print('*', end="")
#         print('')
#     else:
#         for j in range(1, i-4+1): # 空格
#             print(' ', end="")
#         for k in range(1, 15-2*i+1):  # *
#             print('*', end="")
#         print('')

for i in range(0, 4):
    for j in range(0, 3-i):
        stdout.write(' ')
    for k in range(0, 2*i+1):
        stdout.write('*')
    print('')
for i in range(0, 3):
    for j in range(0, i+1):
        stdout.write(' ')
    for k in range(0, 5-2*i):
        stdout.write('*')
    print('')