# coding: utf-8
#  时间函数举例2
# time.clock(): 在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
# （实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）

if __name__ == "__main__":
    import time

    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()

    print(end - start)

    start1 = time.clock()
    for i in range(3000):
        print(i)

    end1 = time.clock()
    print('different is %6.3f' % (end1 - start1))