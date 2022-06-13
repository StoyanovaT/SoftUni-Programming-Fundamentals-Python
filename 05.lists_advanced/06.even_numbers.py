numbers = input().split(", ")
numbers = list(map(int, numbers))
even_index_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_index_numbers.append(i)

print(even_index_numbers)


# на това решение излиза 80/100
# numbers = list(map(int, input().split(", ")))
#
# result = [numbers.index(num) for num in numbers if num % 2 == 0 and num != 0]
#
# print(result)
