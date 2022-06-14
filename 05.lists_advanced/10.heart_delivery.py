def representation_data(data, last_position):
    result = [x for x in data if x == 0]
    print(f"Cupid's last position was {last_position}.")
    if len(result) != len(data):
        diff = len(data) - len(result)
        print(f"Cupid has failed {diff} places.")
    else:
        print("Mission was successful.")


def heart_delivery(data):
    current_index_position = 0
    cupids_last_position = 0

    while True:
        command = input().split(" ")

        if command[0] == "Love":
            break

        index = int(command[1]) + current_index_position

        if index >= len(data):
            index = 0

        if -1 < index < len(data):
            if data[index] > 0:
                data[index] -= 2
                if data[index] == 0:
                    print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")
        cupids_last_position = index
        current_index_position = index

    representation_data(data, cupids_last_position)

nums = list(map(int, input().split("@")))
heart_delivery(nums)

# houses = input().split("@")
# houses = list(map(int, houses))
# line = input()
# successful = True
# already_had_valentine = False
# current_house = 0
# counter = 0
# while line != "Love!":
#
#     command = line.split(" ")
#     jump_length = int(command[1])
#     current_house += jump_length
#
#     if current_house >= len(houses):
#         current_house = 0
#
#     if houses[current_house] == 0:
#         print(f"Place {current_house} already had Valentine's day.")
#
#     else:
#         houses[current_house] -= 2
#         if houses[current_house] == 0:
#             print(f"Place {current_house} has Valentine's day.")
#
#     line = input()
#
# print(f"Cupid's last position was {current_house}.")
# for i in houses:
#     if i > 0:
#         counter += 1
#         successful = False
# if successful:
#     print("Mission was successful.")
# else:
#     print(f"Cupid has failed {counter} places.")
