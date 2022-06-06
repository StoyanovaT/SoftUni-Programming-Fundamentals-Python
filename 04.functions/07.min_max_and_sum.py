def min_max_sum(num):
    print(f"The minimum number is {min(numbers)}")
    print(f"The maximum number is {max(numbers)}")
    print(f"The sum number is: {sum(numbers)}")


numbers = list(map(int, input().split(" ")))
min_max_sum(numbers)
