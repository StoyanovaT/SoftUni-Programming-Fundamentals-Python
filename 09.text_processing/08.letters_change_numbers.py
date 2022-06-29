# text = input().split()
#
# total = 0
#
# for i in text:
#     word = i.strip()
#     working_num = int(word[1:-1])
#     first_letter = word[0]
#     last_letter = word[-1]
#
#     if first_letter.isupper():
#         divisor = ord(first_letter) - 64
#         working_num /= divisor
#     elif first_letter.islower():
#         multiplier = ord(first_letter) - 96
#         working_num *= multiplier
#
#     if last_letter.isupper():
#         subtract = ord(last_letter) - 64
#         working_num -= subtract
#     elif last_letter.islower():
#         add_num = ord(last_letter) - 96
#         working_num += add_num
#
#     total += working_num
#
# print(f"{total:.2f}")

# Mario
from string import ascii_lowercase


def extract_func(text):
    current_num = [num for num in text if num.isdigit()]
    result = 0

    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1

            if i == 0:
                if text[i] == text[i].lower():
                    result = int(''.join(current_num)) * index
                else:
                    result = int(''.join(current_num)) / index
            else:
                if text[i] == text[i].lower():
                    result += index
                else:
                    result -= index

    return result


def letters_change_numbers(data):
    result = 0

    for num in data:
        result += extract_func(num)
    print(f"{result:.2f}")


data = input().split()
letters_change_numbers(data)