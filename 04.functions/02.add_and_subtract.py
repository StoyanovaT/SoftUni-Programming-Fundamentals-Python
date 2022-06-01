def sum_numbers(a, b):
    return a + b


def subtract(current_sum, c):
    return current_sum - c


a, b, c = int(input()), int(input()), int(input())
result = subtract(sum_numbers(a, b), c)
print(result)


# def sum_numbers(a, b):
#     return a + b
#
#
# def subtract(sum_nums, c):
#     return sum_nums - c
#
#
# def add_and_subtract(sum_nums, subtr):
#     return subtr
#
#
# num1, num2, num3 = int(input()), int(input()), int(input())
#
# print(add_and_subtract(sum_numbers(num1, num2), subtract(sum_numbers(num1, num2), num3)))
