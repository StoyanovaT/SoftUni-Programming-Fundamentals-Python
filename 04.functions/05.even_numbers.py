# result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" ")))))
# print(result)

# def check_even(number):
#     if number % 2 == 0:
#         return True
#
#     return False
#
#
# numbers = list(map(int, input().split(" ")))
#
# even_numbers = filter(check_even, numbers)
# even_nums_list = list(even_numbers)
#
# print(even_nums_list)

def check_even(number):
    if number % 2 == 0:
        return True

    return False


result = filter(check_even, list(map(int, input().split(" "))))
print(list(result))
