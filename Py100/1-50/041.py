# coding: utf-8
# 题目：模仿静态变量的用法。

# 类属性/实例属性： https://blog.csdn.net/Leo_Coding/article/details/72935271

# “静态”变量： https://www.cnblogs.com/turtle-fly/p/3280610.html

# python实现静态变量： https://blog.csdn.net/DawnRanger/article/details/78306878

class task_queue:
    queue = []     # 类的属性

    def append(self, obj):
        self.queue.append(obj)

    def print_queue(self):
        print(self.queue)


if __name__ == "__main__":
    a = task_queue()
    b = task_queue()
    c = task_queue()

    a.append('tc_1')  # queue 中添加了 'tc_1'

    a.print_queue()
    b.print_queue()  # b 和 c 获取的 queue 依然是公共的 类的属性
    c.print_queue()




def varfunc():
    var = 0      # 动态变量
    print("var = %d" %var)
    var += 1
if __name__ == "__main__":
    for i in range(3):
        varfunc()


# 在类中定义在函数外面的变量是类变量，不属于类的实例。利用它可以实现静态变量。
class Static:
    var = 5   # 类的属性
    def varfunc1(self):
        self.var += 1
        print(self.var)

print(Static.var)
a = Static()
for i in range(4):
    a.varfunc1()