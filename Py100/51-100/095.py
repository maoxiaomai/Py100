# coding: utf-8
# 字符串日期转换为易读的日期格式。

import time

date = "Aug 28 2015 12:00AM"
struct_time = time.strptime(date, "%b %d %Y %I:%M%p")
print(struct_time)
formated_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
print(formated_time)