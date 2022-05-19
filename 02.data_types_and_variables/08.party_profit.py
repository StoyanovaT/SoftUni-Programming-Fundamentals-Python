import math

group = int(input())
days = int(input())
tot_coins = 0

for i in range(1, days + 1):
    if i % 15 == 0:
        group += 5
    if i % 10 == 0:
        group -= 2
    tot_coins += (50 - (group * 2))
    if i % 5 == 0:
        tot_coins += (group * 20)
        if i % 3 == 0:
            tot_coins -= group * 2
    if i % 3 == 0:
        tot_coins -= (group * 3)

coins_each = tot_coins // group

print(f"{group} companions received {coins_each} coins each.")
