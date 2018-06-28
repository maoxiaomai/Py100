# -*- coding: utf-8 -*-
# 把列表a种的元素复制到b
def copy1(a):
    b = a[:]
    print(b)

copy1([1,2,3,4])

def copy2(a):
    b = a.copy()
    print(b)

copy2([1,2,3,4,5])