import re
text = input()
tot_calories = 0
items = []
regex = r"(\#|\|)([A-Za-z ]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1"

matches = re.finditer(regex, text)
for match in matches:
    item = match.group(2)
    date = match.group(3)
    calories = int(match.group(4))

    tot_calories += calories

    items.append(item)
    items.append(date)
    items.append(calories)


days = tot_calories // 2000

print(f"You have food to last you for: {days} days!")

for i in range(0, len(items)-2, 3):
    print(f"Item: {items[i]}, Best before: {items[i+1]}, Nutrition: {items[i+2]}")
