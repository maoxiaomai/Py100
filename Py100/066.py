# coding: utf-8
# 题目：输入3个数a,b,c，按大小顺序输出。

a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

L = []
L.append(a)
L.append(b)
L.append(c)
L.sort()
for i in L:
    print(i)


# method2
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a,b,c)


# method3
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(a,b,c)


# maopao:
list=[a,b,c]
for i in range(0, len(list)-1):
    for j in range(0, len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(L)