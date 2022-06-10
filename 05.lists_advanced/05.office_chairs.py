def office_management(number_of_rooms):
    left_chairs = 0
    condition = True

    for room_number in range(1, number_of_rooms + 1):
        data = input().split(" ")
        available_chairs = data[0]
        visitors = int(data[1])

        diff = abs(len(available_chairs) - visitors)

        if len(available_chairs) < visitors:
            condition = False
            print(f"{diff} more chair needed in room {room_number}")

        elif len(available_chairs) > visitors:
            left_chairs += diff
    if condition:
        print(f"Game On, {left_chairs} free chairs left")


info = int(input())
office_management(info)


# rooms = int(input())
# room_number = 1
# free_chairs = 0
# enough_chairs = True
# for room in range(rooms):
#     data = input().split(" ")
#     chairs = len(data[0])
#     visitors = int(data[1])
#     if chairs < visitors:
#         chairs_needed = visitors - chairs
#         print(f"{chairs_needed} more chairs needed in room {room_number}")
#         enough_chairs = False
#
#     else:
#         free_chairs += chairs - visitors
#     room_number += 1
#
# if enough_chairs:
#     print(f"Game On, {free_chairs} free chairs left")
