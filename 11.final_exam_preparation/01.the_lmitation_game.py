message = input()
command = input()

while command != "Decode":
    command_params = command.split("|")

    if command_params[0] == "Move":
        location = int(command_params[1])
        movement = message[:location]
        static = message[location:]
        message = static + movement

    elif command_params[0] == "Insert":
        index = int(command_params[1])
        value = command_params[2]
        before = message[:index]
        after = message[index:]
        message = before + value + after

    elif command_params[0] == "ChangeAll":
        current_substr = command_params[1]
        replacement = command_params[2]
        message = message.replace(current_substr, replacement)

    command = input()

print(f"The decrypted message is: {message}")


# moe reshenie predi lekciyata
# message = input()
# command = input()
# message_working_copy = ""
# while command != "Decode":
#     instruction = command.split("|")
#
#     if instruction[0] == "Move":
#         num_of_letters = instruction[1]
#         message_working_copy = message[int(instruction[1]):] + message[:int(instruction[1])]
#         message = message_working_copy
#         message_working_copy = ""
#
#     elif instruction[0] == "Insert":
#         if int(instruction[1]) == len(message):
#             message += instruction[2]
#         else:
#             for i in range(len(message)):
#                 if i < int(instruction[1]):
#                     message_working_copy += message[i]
#                 elif i == int(instruction[1]):
#                     message_working_copy += instruction[2]
#                     message_working_copy += message[i]
#                 else:
#                     message_working_copy += message[i]
#             message = message_working_copy
#             message_working_copy = ""
#
#     else:
#         for i in message:
#             if i == instruction[1]:
#                 message_working_copy += instruction[2]
#             else:
#                 message_working_copy += i
#         message = message_working_copy
#         message_working_copy = ""
#
#     command = input()
#
# print(f"The decrypted message is: {message}")