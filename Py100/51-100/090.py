# coding: utf-8
# 列表使用实例

#list
#新建列表
testList=[10086,'中国移动',[1,2,4,5]]

# 访问列表长度
print(len(testList))

print(testList[1:])

testList.append('i\'m new here!')

print(len(testList))

print(testList[-1])

testList.pop()

print(len(testList))

print(testList)

#list comprehension
#后面有介绍，暂时掠过
matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
print(matrix)
print(matrix[1])
col2 = [row[1] for row in matrix] #get a  column from a matrix
print(col2)
col2even = [row[1] for row in matrix if  row[1] % 2 == 0]#filter odd item
print(col2even)