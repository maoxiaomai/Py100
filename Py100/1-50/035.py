# -*- coding: utf-8 -*-
# 题目：文本颜色设置。

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'   # <!--采用终端默认设置，即取消颜色设置-->
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.FAIL + "什么颜色" )
print('aaaaa' + bcolors.ENDC)
print('wwww')  # 变回终端默认颜色
print(bcolors.OKGREEN + "OK" + bcolors.ENDC)