# numbers_str = input()
# nums_list = []
#
# nums_list.append(numbers_str)
# nums_list = numbers_str.split()
#
# for n in range(len(nums_list)):
#     nums_list[n] = int(nums_list[n]) * -1
#
# print(nums_list)

# или:

# print(list(-int(x) for x in input().split()))

# или

# numbers = input().split()
# list = []
# for number in numbers:
#     current_number = int(number)
#     list.append(-current_number)
# print(list)

nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(" ")))]
print(nums)