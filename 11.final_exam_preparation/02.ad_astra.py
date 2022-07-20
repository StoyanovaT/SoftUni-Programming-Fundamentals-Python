import re

info = input()
pattern = '\#([a-z A-Z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|' \
          '\|([a-z A-Z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'
result = re.findall(pattern, info)
items = []
calories = 0

for item in result:
    current_item = [el for el in item if el != '']
    items.append(current_item)
    calories += int(current_item[2])

number_of_days = int(calories / 2000)

print(f'You have food to last you for: {number_of_days} days!')

for data in items:
    product = data[0]
    date = data[1]
    current_calories = data[2]
    print(f'Item: {product}, Best before: {date}, Nutrition: {current_calories}')

# moe reshenie predi lekciqta
# import re
# total_calories = 0
#
# items_info = []
#
# text = input()
#
# regex = r"(\#|\|)(?P<item>[a-zA-Z ]+)\1(?P<best_before>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]+)\1"
#
# matches = re.finditer(regex, text)
#
# for match in matches:
#     item = match.group("item")
#     best_before = match.group("best_before")
#     calories = int(match.group("calories"))
#     items_info.append(item)
#     items_info.append(best_before)
#     items_info.append(calories)
#     total_calories += calories
#
#
# days = total_calories//2000
#
# print(f"You have food to last you for: {days} days!")
#
# for i in range(0, (len(items_info) - 2), 3):
#     print(f"Item: {items_info[i]}, Best before: {items_info[i+1]}, Nutrition: {items_info[i+2]}")
