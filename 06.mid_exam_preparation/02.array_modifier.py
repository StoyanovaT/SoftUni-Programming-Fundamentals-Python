numbers = list(map(int, input().split(" ")))

command = input()

while command != "end":
    if command == "decrease":
        numbers = list(map(lambda n: n - 1, numbers))

    else:
        command = command.split(" ")
        action = command[0]
        index1 = int(command[1])
        index2 = int(command[2])

        if action == "swap":
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

        elif action == "multiply":
            numbers[index1] = numbers[index1] * numbers[index2]

    command = input()

numbers = list(map(str, numbers))
output = ", ".join(numbers)
print(output)
