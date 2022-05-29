n = int(input())
word = str(input())
full_list = []
matches_list = []
for _ in range(n):
    string = str(input())
    full_list.append(string)

print(full_list)

for match in full_list:
    if word in match:
        matches_list.append(match)

print(matches_list)

# или
# number = int(input())
# search_word = input()
# strings = list()
# filtered = list()
#
# for i in range(number):
#     current_string = input()
#     strings.append(input())
#     if search_word in current_string:
#         filtered.append(current_string)
#
# print(strings)
# print(filtered)

