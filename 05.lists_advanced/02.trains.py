num_wagons = int(input())
train = [0 for i in range(num_wagons)]

command = input()

while command != "End":
    explode = command.split(" ")
    current = explode[0]
    if current == "add":
        num_people = int(explode[1])
        train[-1] += num_people

    if current == "insert":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] += num_people
    if current == "leave":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] -= num_people
    command = input()

print(train)

# number_of_wagons = int(input())
# train = [0 for num in range(number_of_wagons)]
#
# line = input()
#
# while line != "End":
#     command = line.split(" ")
#     if command[0] == "add":
#         people = int(command[1])
#         train[-1] += people
#
#     else:
#         index = int(command[1])
#         people = int(command[2])
#
#         if command[0] == "insert":
#             train[index] += people
#
#         elif command[0] == "leave":
#             train[index] -= people
#
#     line = input()
#
# print(train)
