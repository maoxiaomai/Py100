# coding: utf-8
# 反向输出一个链表。

if __name__ == "__main__":
    ptr = []
    for i in range(0, 5):
        ptr.append(int(input("Please enter a number: ")))
    print(ptr)
    ptr.reverse()
    print(ptr)
