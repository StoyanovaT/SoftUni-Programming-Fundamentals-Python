def odd_even_sum(nums):
    odd_sum = 0
    even_sum = 0
    for i in numbers:
        if i % 2 != 0:
            odd_sum += i
        else:
            even_sum += i
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


numbers = list(map(int, input()))
# numbers = map(int, list(input()))
odd_even_sum(numbers)
