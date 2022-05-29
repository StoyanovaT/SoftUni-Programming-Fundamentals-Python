events = input().split("|")
energy = 100
coins = 100
condition = True

for event in events:
    current_command = event.split("-")
    command = current_command[0]
    number = int(current_command[1])

    if command == "rest":
        if energy + number <= 100:
            gained_energy = number
            energy += gained_energy
        else:
            gained_energy = 0
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif command == "order":
        if energy >= 30:
            energy -= 30
            earned_coins = number
            coins += earned_coins
            print(f"You earned {earned_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            condition = False
            break

if condition:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
