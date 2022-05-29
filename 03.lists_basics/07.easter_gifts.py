gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    command = command.split()

    if "OutOfStock" in command:
        for i in range(len(gifts)):
            if str(gifts[i]) == str(command[1]):
                gifts[i] = "None"

    elif "Required" in command:
        if 0 <= int(command[2]) <= len(gifts):
            gifts[int(command[2])] = command[1]

    elif "JustInCase" in command:
        gifts[-1] = command[1]


for j in gifts:
    if not j == "None":
        print(j, end=" ")
