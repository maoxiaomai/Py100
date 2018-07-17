# coding: utf-8
# 遍历字典
# 找到年龄最大的人，并输出。

if __name__ == "__main__":
    person = {"li":18, "wang":50, "zhang":20, "sun":22}
    m = "li"
    for key in person:
        if person[key] > person[m]:
            m = key
    print('%s, %d' %(m, person[m]))
    for key in person.keys():
        print(key)
    for key,value in person.items():
        print(key,value)
    for value in person.values():
        print(value)
