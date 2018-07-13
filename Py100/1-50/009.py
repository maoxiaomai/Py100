# coding: utf-8
# 题目：国际象棋棋盘由64个黑白相间的格子组成，分为8行*8列。
# 程序分析：用i控制行，j来控制列，根据i+j的和的变化来控制输出黑方格，还是白方格。

import sys

for i in range(0,8):
    for j in range(0,8):
        k = i + j
        if k % 2 ==0:
            sys.stdout.write('■')
        else:
            sys.stdout.write("□")
    print('')