# coding: utf-8
#

class Student:
    x = 0
    c = 0

def f(stu):
    stu.x = 20
    stu.c = 'c'

a = Student()
print(a.x, a.c)  # a.x = 0  c.x = 0

a.x = 3
a.c = 'a'
print(a.x, a.c)  # a.x = 3  c.x = a

f(a)
print(a.x, a.c)  # a.x = 20  c.x = c