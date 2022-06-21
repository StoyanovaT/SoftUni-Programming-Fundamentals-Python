num_of_commands = int(input())
parking_dict = {}

for i in range(num_of_commands):
    info = input().split(" ")

    if info[0] == "register":
        username = info[1]
        plate_number = info[2]
        if username in parking_dict:
            print(f"ERROR: already registered with plate number {parking_dict[username]}")
        else:
            parking_dict[username] = plate_number
            print(f"{username} registered {parking_dict[username]} successfully")


    else:
        username = info[1]
        if username not in parking_dict:
            print(f"ERROR: user {username} not found")
        else:
            del parking_dict[username]
            print(f"{username} unregistered successfully")

for key, value in parking_dict.items():
    print(f"{key} => {value}")
