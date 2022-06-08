def factorial(num):
    # return 1 if num == 0 or num == 1 else num * factorial(num - 1)

    f = 1
    if num >= 1:
        for i in range(1, num + 1):
            f = f * i
    return f


num1 = int(input())
num2 = int(input())
result = factorial(num1) / factorial(num2)
print(f"{result:.2f}")

# def factorial_division(a, b):
#     fact_1 = 1
#     fact_2 = 1
#     for n1 in range(num_1, 0, -1):
#         fact_1 *= n1
#
#     for n2 in range(num_2, 0, -1):
#         fact_2 *= n2
#
#     division = fact_1 / fact_2
#     print(f"{division:.2f}")
#
#
# num_1 = int(input())
# num_2 = int(input())
# factorial_division(num_1, num_2)
