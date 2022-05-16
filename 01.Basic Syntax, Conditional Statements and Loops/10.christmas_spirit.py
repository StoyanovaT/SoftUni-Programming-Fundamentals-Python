quantity = int(input())
days = int(input())

tot_cost = 0
tot_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        tot_cost += 2 * quantity
        tot_spirit += 5
    if day % 3 == 0:
        tot_cost += (5 * quantity) + (3 * quantity)
        tot_spirit += 13
    if day % 5 == 0:
        tot_cost += (15 * quantity)
        tot_spirit += 17
        if day % 3 == 0:
            tot_spirit += 30
    if day % 10 == 0:
        tot_spirit -= 20
        tot_cost += 23

if days % 10 == 0:
    tot_spirit -= 30


print(f"Total cost: {tot_cost}")
print(f"Total spirit: {tot_spirit}")