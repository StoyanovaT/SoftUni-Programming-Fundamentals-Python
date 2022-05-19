balls = int(input())
h_value = 0
h_weight = 0
h_time = 0
h_quality = 0

for b in range(balls):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality
    if value > h_value:
        h_value = value
        h_weight = weight
        h_time = time
        h_quality = quality

print(f"{h_weight} : {h_time} = {int(h_value)} ({h_quality})")

# Решение на Марио
# number_of_snowballs = int(input())
# best_snowball_quality = 0
# best_snowball_data = ""
#
# for _ in range(number_of_snowballs):
#     weight = int(input())
#     time = int(input())
#     quality = int(input())
#
#     result = (weight / time) ** quality
#
#     if result > best_snowball_quality:
#         best_snowball_quality = result
#         best_snowball_data = f"{weight} : {time} = {int(result)} ({quality})"
#
# print(best_snowball_data)