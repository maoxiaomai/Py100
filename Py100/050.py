# coding: utf-8
# 输出一个随机数。
# 生成 10 到 20 之间的随机数
import random

num = random.uniform(10,20)
print(num)

print(random.randint(1,10))        # 产生 1 到 10 的一个整数型随机数
print(random.random())             # 产生 0 到 1 之间的随机浮点数
print(random.uniform(1.1,5.4))     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print(random.choice('tomorrow'))   # 从序列中随机选取一个元素
print(random.randrange(1,100,2))   # 生成从1到100的间隔为2的随机整数
