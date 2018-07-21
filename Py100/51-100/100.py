# coding: utf-8
# 列表转换为字典

list1 = ['key1', 'key2', 'key3']
list2 = [1, 2, 3]
list_new = dict(zip(list1, list2))
print(list_new)
