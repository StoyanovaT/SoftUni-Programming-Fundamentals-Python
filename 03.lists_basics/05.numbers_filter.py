n = int(input())
numbers_list = []
filtered = []
for _ in range(n):
    number = int(input())
    numbers_list.append(number)

command = str(input())

for num in numbers_list:
    if command == "even":
        if num % 2 == 0 or num == 0:
            filtered.append(num)

    elif command == "odd":
        if num % 2 != 0:
            filtered.append(num)

    elif command == "negative":
        if num < 0:
            filtered.append(num)

    elif command == "positive":
        if num >= 0:
            filtered.append(num)

print(filtered)

# или:

# n = int(input())
# positive = []
# negative = []
# odd = []
# even = []
#
# filtered = []
# for _ in range(n):
#     number = int(input())
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
#     if number >= 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# command = str(input())
# if command == "even":
#     print(even)
#
# elif command == "odd":
#     print(odd)
#
# elif command == "negative":
#     print(negative)
#
# elif command == "positive":
#     print(positive)

# или ред 50 до 60 ги заместваме с:
# print(eval(command))
