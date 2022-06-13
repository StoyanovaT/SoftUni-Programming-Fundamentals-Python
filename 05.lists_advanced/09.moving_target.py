targets = list(map(int, input().split(" ")))

line = input()

while line != "End":
    command = line.split(" ")
    action = command[0]
    index1 = int(command[1])
    index2 = int(command[2])

    if action == "Shoot":
        if 0 <= index1 <= len(targets):
            current_target = targets[index1]
            current_target -= index2
            if current_target <= 0:
                targets.pop(index1)
            else:
                targets[index1] = current_target

    elif action == "Add":
        if 0 <= index1 < len(targets):
            targets.insert(index1, index2)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if index1 + index2 < len(targets) and index1 - index2 >= 0:
            targets = targets[:index1 - index2] + targets[index1 + index2 + 1:]
        else:
            print("Strike missed!")

    line = input()

targets = list(map(str, targets))
print("|".join(targets))
