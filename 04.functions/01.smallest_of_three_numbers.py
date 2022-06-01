# def smallest_num(a, b, c):
#     if num_1 < num_2 and num_1 < num_3:
#         return num_1
#     elif num_2 < num_1 and num_2 < num_3:
#         return num_2
#     elif num_3 < num_1 and num_3 < num_2:
#         return num_3
#
#
# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
#
# print(smallest_num(num_1, num_2, num_3))

# import sys
#
#
# def smallest_num(a,b,c):
#     nums_list = []
#     min_num = sys.maxsize
#
#     nums_list.append(num_1)
#     nums_list.append(num_2)
#     nums_list.append(num_3)
#     for num in nums_list:
#         if min_num > num:
#             min_num = num
#     return min_num
#
#
# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
#
# print(smallest_num(num_1,num_2,num_3))

def smallest_num(a, b, c):
    return min(a, b, c)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(smallest_num(num_1, num_2, num_3))
