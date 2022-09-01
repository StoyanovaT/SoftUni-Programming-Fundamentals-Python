count = int(input())
heroes = dict()

for i in range(count):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hp = "HP"
    mp = "MP"
    hero_HP = int(current_hero[1])
    hero_MP = int(current_hero[2])

    current_hero_dict = dict()
    current_hero_dict[hp] = hero_HP
    current_hero_dict[mp] = hero_MP
    heroes[hero_name] = current_hero_dict

command = input()

while command != "End":
    command_params = command.split(" - ")
    command_name = command_params[0]
    hero_name = command_params[1]
    value = int(command_params[2])

    if command_name == "Heal":
        if heroes[hero_name]["HP"] + value > 100:
            value = 100 - heroes[hero_name]["HP"]
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += value

        print(f"{hero_name} healed for {value} HP!")

    elif command_name == "Recharge":
        if heroes[hero_name]["MP"] + value > 200:
            value = 200 - heroes[hero_name]["MP"]
            heroes[hero_name]["MP"] = 200
        else:
            heroes[hero_name]["MP"] += value

        print(f"{hero_name} recharged for {value} MP!")

    elif command_name == "TakeDamage":
        attacker = command_params[3]
        heroes[hero_name]["HP"] -= value
        if heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {value} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command_name == "CastSpell":
        spell = command_params[3]
        if heroes[hero_name]["MP"] >= value:
            heroes[hero_name]["MP"] -= value
            print(f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")

    command = input()

for hero in heroes:
    print(f"{hero}")
    print(f"  HP: {heroes[hero]['HP']}")
    print(f"  MP: {heroes[hero]['MP']}")

# moe reshenie predi lekciyata
# number_of_heroes = int(input())
# heroes_dict = {}
#
# for _ in range(number_of_heroes):
#     heroes_info = input().split()
#     hero_name = heroes_info[0]
#     hit_points = int(heroes_info[1])
#     mana_points = int(heroes_info[2])
#
#     heroes_dict[hero_name] = [hit_points, mana_points]
#
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     actions = command.split(" - ")
#
#     if actions[0] == "CastSpell":
#         hero = actions[1]
#         mp_needed = int(actions[2])
#         spell_name = actions[3]
#
#         if heroes_dict[hero][1] >= mp_needed:
#             heroes_dict[hero][1] -= mp_needed
#             print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero][1]} MP!")
#         else:
#             print(f"{hero} does not have enough MP to cast {spell_name}!")
#
#     elif actions[0] == "TakeDamage":
#         hero = actions[1]
#         damage = int(actions[2])
#         attacker = actions[3]
#
#         if heroes_dict[hero][0] <= damage:
#             del heroes_dict[hero]
#             print(f"{hero} has been killed by {attacker}!")
#         else:
#             heroes_dict[hero][0] -= damage
#             print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero][0]} HP left!")
#
#     elif actions[0] == "Recharge":
#         hero = actions[1]
#         amount = int(actions[2])
#
#         if heroes_dict[hero][1] + amount > 200:
#             print(f"{hero} recharged for {200 - heroes_dict[hero][1]} MP!")
#             heroes_dict[hero][1] = 200
#         else:
#             heroes_dict[hero][1] += amount
#             print(f"{hero} recharged for {amount} MP!")
#
#     elif actions[0] == "Heal":
#         hero = actions[1]
#         amount = int(actions[2])
#
#         if heroes_dict[hero][0] + amount > 100:
#             print(f"{hero} healed for {100 - heroes_dict[hero][0]} HP!")
#             heroes_dict[hero][0] = 100
#         else:
#             heroes_dict[hero][0] += amount
#             print(f"{hero} healed for {amount} HP!")
#
# for (hero, points) in heroes_dict.items():
#     print(hero)
#     print(f"  HP: {points[0]}")
#     print(f"  MP: {points[1]}")
