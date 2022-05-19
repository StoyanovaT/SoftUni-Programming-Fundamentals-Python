n = int(input())

for num in range(1, n + 1):
    working_num = num
    digit_sum = 0
    while working_num > 0:
        digit_sum += working_num % 10
        working_num = working_num // 10

    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
    print(f"{num} -> {is_special}")
