# coding: utf-8
# 时间函数举例1。
# https://blog.csdn.net/you_are_my_dream/article/details/61616465


if __name__ == "__main__":
    import time

    print(time.time())  # 返回当前时间的时间戳
    print(time.localtime())  # 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
    print(time.localtime(time.time()))
    print(time.gmtime()) # 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
    print(time.asctime(time.localtime(time.time()))) # 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。如果没有参数，将会将time.localtime()作为参数传入。
    print(time.asctime(time.gmtime(time.time())))
    print(time.ctime()) # 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候， \
    # 将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。

    print(time.strftime("%Y-%m-%d %X", time.localtime())) # 把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。
    # 如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。

    print(time.strptime('2018-07-17 19:18:34', "%Y-%m-%d %X")) # 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。