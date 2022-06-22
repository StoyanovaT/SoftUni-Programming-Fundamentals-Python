def create_force_side(side, member, user_info_dict):
    condition = [current_side for current_side in user_info_dict if member in user_info_dict[current_side]]

    if len(condition) == 0:
        condition.clear()
        if side not in user_info_dict:
            user_info_dict[side] = [member]
        else:
            user_info_dict[side].append(member)

    return user_info_dict


def create_force_user(member, side, user_info_dict):
    for current_side in user_info_dict:
        if member in user_info_dict[current_side]:
            if len(user_info_dict[current_side]) > 1:
                user_info_dict[current_side].pop(member)
                break

            else:
                del user_info_dict[current_side]
                break
    if side in user_info_dict:
        user_info_dict[side].append(member)
    else:
        user_info_dict[side] = [member]

    print(f"{member} joins the {side} side!")


def force_book():
    user_info_dict = {}

    while True:
        command = input()

        if command == "Lumpawaroo":
            break

        if "|" in command:
            command = command.split(" | ")
            side = command[0]
            member = command[1]
            create_force_side(side, member, user_info_dict)

        elif "->" in command:
            command = command.split(" -> ")
            member = command[0]
            side = command[1]
            create_force_user(member, side, user_info_dict)

    for data in user_info_dict:
        print(f"Side: {data}, Members: {len(user_info_dict[data])}")
        for name in user_info_dict[data]:
            print(f"! {name}")


force_book()

#мое решение дава 80/100:
# profiles_dict = {}
#
# while True:
#     info = input()
#
#     if info == "Lumpawaroo":
#         break
#
#     if "|" in info:
#         info = info.split(" | ")
#         force_side = info[0]
#         user = info[1]
#
#         if force_side not in profiles_dict.keys() and user not in profiles_dict.values():
#             profiles_dict[force_side] = [user]
#
#         else:
#             exist = False
#             for key in profiles_dict.keys():
#                 if user in profiles_dict[key]:
#                     exist = True
#                     break
#             if not exist:
#                 profiles_dict[force_side].append(user)
#
#     else:
#         info = info.split(" -> ")
#         force_side = info[1]
#         user = info[0]
#
#         if force_side not in profiles_dict.keys() and user not in profiles_dict.values():
#             profiles_dict[force_side] = [user]
#
#         else:
#             condition = False
#             for key in profiles_dict.keys():
#                 if user in profiles_dict[key]:
#                     condition = True
#                     break
#             if condition:
#                 for key in profiles_dict.keys():
#                     for value in profiles_dict[key]:
#                         if value == user:
#                             current_side = key
#                             profiles_dict[key].remove(value)
#                             for k in profiles_dict.keys():
#                                 if k != current_side:
#                                     profiles_dict[k].append(user)
#                                     force_side = k
#
#             else:
#                 profiles_dict[force_side].append(user)
#
#         print(f"{user} joins the {force_side} side!")
#
# for key in profiles_dict.keys():
#     if len(profiles_dict[key]) != 0:
#         print(f"Side: {key}, Members: {len(profiles_dict[key])}")
#         for u in profiles_dict[key]:
#             print(f"! {u}")
