import sys

factor = int(input())
count = int(input())
list = []

for num in range(factor, sys.maxsize):
    if num / factor == num // factor:
        list.append(num)
    if len(list) == count:
        break

print(list)

# или:
# num1 = int(input())
# num2 = int(input())
# new_list = []
# for num in range(1, num2 + 1):
#     new_list.append(num * num1)
#
# print(new_list)

# или:
# import sys
#
# factor = int(input())
# count = int(input())
# multiples = []
#
# for i in range(factor, sys.maxsize):
#     if i % factor == 0:
#         multiples.append(i)
#         if len(multiples) == count:
#             break
#
# print(multiples)