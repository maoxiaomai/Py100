# -*- coding: utf-8 -*-
# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
import re

char = input("Please input string: ")
num_count = 0
letter_count = 0
space_count = 0
others_count = 0
for c in char:
    if re.match(r'[0-9]', c):       # c.isdigit():
        num_count += 1
    elif re.match(r'[a-zA-Z]', c):  # c.isalpha():
        letter_count += 1
    elif c == ' ':                  # c.isspace():
        space_count += 1
    else:
        others_count += 1

print("digits=%d, char=%d, space=%d, others=%d" %(num_count, letter_count, space_count, others_count))