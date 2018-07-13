# coding: utf-8
# 使用lambda来创建匿名函数。

foo = [1,2,3,4,5,6,7]
print(list(map(lambda x: 2*x, foo)))


MAX = lambda x, y : (x>y)*x + (x<y)*y
MIN = lambda x, y : (x<y)*x + (x>y)*y

if __name__ == '__main__':
    a = 10
    b = 20
    print('The larger one is %d' % MAX(a, b))
    print('The lower one is %d' % MIN(a, b))