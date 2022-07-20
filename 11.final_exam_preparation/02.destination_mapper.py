import re

text = input()
regex = r"(?P<delimiter>[=//])([A-Z][A-Za-z]{2,})(?P=delimiter)"

matches = re.finditer(regex, text)
locations = list()
points = 0

for match in matches:
    city = match[2]
    locations.append(city)
    points += len(city)

output_locations = ", ".join(locations)
print(f"Destinations: {output_locations}")
print(f"Travel Points: {points}")

# Moe reshenie predi lekciyata:
# import re
#
# def destination_mapper():
#     points = 0
#     destination_list = []
#     info = input()
#     regex = r"(?<=(\=|\/))(?P<place>[A-Z][A-Za-z][A-Za-z]+)(?=(\1))"
#     matches = re.finditer(regex, info)
#     for match in matches:
#         place = match.group("place")
#         destination_list.append(place)
#
#     for i in destination_list:
#         points += len(i)
#     final_destinations = ", ".join(destination_list)
#     print(f"Destinations: {final_destinations}")
#     print(f"Travel Points: {points}")
#
#
# destination_mapper()
