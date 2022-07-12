import re
demons_dict = {}

text = input().split(",")
for d in text:
    demon = d.strip()
    current_health = 0
    regex_health = r"[^\+\-\*\/\.0-9]"
    matches_health = re.findall(regex_health, demon)
    for i in matches_health:
        current_health += ord(i)

    regex_damage_nums = r"(?P<nums>-?[0-9]+(\.[0-9]+)?)"
    regex_actions = r"([\*\/])"
    matches_damage = re.finditer(regex_damage_nums, demon)
    current_damage = 0
    nums = []
    for n in matches_damage:
        num = float(n.group("nums"))
        nums.append(num)
    current_damage += sum(nums)

    matches_actions = re.finditer(regex_actions, demon)
    for a in matches_actions:
        action = a.group(1)
        if action == "*":
            current_damage *= 2
        elif action == "/":
            current_damage /= 2

    demons_dict[demon] = []
    demons_dict[demon].append(current_health)
    demons_dict[demon].append(current_damage)

sorted(demons_dict.keys())
for key in sorted(demons_dict.keys()):
    print(f"{key} - {demons_dict[key][0]} health, {demons_dict[key][1]:.2f} damage")
