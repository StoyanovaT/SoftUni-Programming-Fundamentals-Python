import re

participants = input().split(", ")

racers_info = dict()

while True:
    info = input()

    if info == "end of race":
        break

    name_finder = r"[a-zA-Z]"
    km_finder = r"[0-9]"
    name_match = re.findall(name_finder, info)
    km_match = re.findall(km_finder, info)

    name_of_racer = "".join(name_match)
    km_list = [int(i) for i in km_match]
    if name_of_racer in participants:
        if name_of_racer in racers_info.keys():
            racers_info[name_of_racer] += sum(km_list)
        else:
            racers_info[name_of_racer] = sum(km_list)

sorted_racers_info = dict(sorted(racers_info.items(), key=lambda item: item[1], reverse=True))

ranking = []
for name in sorted_racers_info.keys():
    if len(ranking) == 3:
        break
    ranking.append(name)


print(f"1st place: {ranking[0]}")
print(f"2nd place: {ranking[1]}")
print(f"3rd place: {ranking[2]}")
