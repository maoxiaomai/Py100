# coding: utf-8
# 八进制转换为十进制

# num = int(input('Input a octal number: '))
# sum = 0
# count = 0
# while num != 0:
#     a = num % 10
#     sum += a * 8**(count)
#     num = num // 10
#     count += 1
#
# print(sum)

num = input('Input a octal number: ')
sum = 0
for i in range(0, len(num)):
    #sum += int(num[i]) * 8**(len(num)-i-1)
    sum = sum * 8 + int(num[i])
print(sum)