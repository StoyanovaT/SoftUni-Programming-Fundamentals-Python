# info = input().split()
# first_word = info[0]
# second_word = info[1]
#
# tot_sum = 0
# if len(first_word) == len(second_word):
#     for ch in range(len(first_word)):
#         tot_sum += ord(first_word[ch]) * ord(second_word[ch])
#
# else:
#     if len(first_word) > len(second_word):
#         longer_word = first_word
#         shorter_word = second_word
#     else:
#         longer_word = second_word
#         shorter_word = first_word
#
#     for ch in range(len(shorter_word)):
#         tot_sum += ord(first_word[ch]) * ord(second_word[ch])
#
#     ch_left = len(longer_word) - len(shorter_word)
#
#     if ch_left == 1:
#         tot_sum += ord(longer_word[len(longer_word) - 1])
#     else:
#         start_index = len(longer_word) - ch_left
#
#         for i in range(start_index, len(longer_word)):
#             tot_sum += ord(longer_word[i])
#
# print(tot_sum)

def sum_func(first_word, second_word):
    total_sum = 0

    for i in range(len(first_word)):
        if i < len(second_word):
            total_sum += ord(first_word[i]) * ord(second_word[i])
        else:
            total_sum += ord(first_word[i])

    return total_sum

def char_multiplier(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = sum_func(first_word, second_word)
    else:
        result = sum_func(second_word, first_word)

    print(result)


data = input().split(" ")
char_multiplier(data[0], data[1])