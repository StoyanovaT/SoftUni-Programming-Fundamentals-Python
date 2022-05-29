# cards_str = input().split()
#
# team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
# is_terminated = False
#
# for player in cards_str:
#     if player in team_a:
#         team_a.remove(player)
#     if player in team_b:
#         team_b.remove(player)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         is_terminated = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#
# if is_terminated:
#     print("Game was terminated")

# или:
#
# string_players = input().split(" ")
# list_one = []
# for i in string_players:
#     list_one.append(i)
# team_one = 11
# team_two = 11
# terminated = False
# new_list = list(set(list_one))
# for i in range(1, 11 + 1):
#     team_one -= int(new_list.count(f"A-{i}"))
#     team_two -= int(new_list.count(f"B-{i}"))
#     if team_one < 7 or team_two < 7:
#         print(f"Team A - {team_one}; Team B - {team_two}")
#         print("Game was terminated")
#         terminated = True
#         break
# if terminated != True:
#     print(f"Team A - {team_one}; Team B - {team_two}")

# или Марио:

info = input().split(" ")
team_a_players = 0
team_b_players = 0
players_loses = []
condition = False

for card in info:
    if card not in players_loses:
        players_loses.append(card)
        if "A" in card:
            team_a_players += 1

        elif "B" in card:
            team_b_players += 1

        if team_a_players <= 7 or team_b_players < 7:
            condition = True
            break


print(f"Team A - {11 - team_a_players}, Team B - {11 - team_b_players}")
if condition:
    print("Game was terminated")