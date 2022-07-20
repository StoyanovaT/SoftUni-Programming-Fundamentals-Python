def world_tour(destinations):
    while True:
        command = input().split(':')

        if command[0] == 'Travel':
            print(f"Ready for world tour! Planned stops: {destinations}")
            break

        elif command[0] == 'Add Stop':
            index = int(command[1])
            string = command[2]

            if 0 <= index <= len(destinations):
                destinations = destinations[:index] + string + destinations[index:]
        elif command[0] == 'Remove Stop':
            start_index = int(command[1])
            end_index = int(command[2])

            if 0 <= start_index <= end_index < len(destinations):
                destinations = destinations[:start_index] + destinations[end_index + 1:]

        elif command[0] == 'Switch':
            old_string = command[1]
            new_string = command[2]

            if old_string in destinations:
                destinations = destinations.replace(old_string, new_string)

        print(destinations)


data = input()
world_tour(data)


# moe reshenie predi lekciyata
# text = input()
#
# while True:
#     info = input()
#
#     if info == "Travel":
#         break
#
#     to_do_info = info.split(":")
#     command = to_do_info[0]
#
#     if command == "Add Stop":
#         index = int(to_do_info[1])
#         str_to_add = to_do_info[2]
#
#         if 0 <= index < len(text):
#             current_text = text[:index] + str_to_add + text[index:]
#             text = current_text
#             print(text)
#         else:
#             print(text)
#
#     elif command == "Remove Stop":
#         start_index = int(to_do_info[1])
#         end_index = int(to_do_info[2])
#
#         if 0 <= start_index < len(text) and 0 <= end_index < len(text) and start_index <= end_index:
#             current_text = text[:start_index] + text[end_index+1:]
#             text = current_text
#             print(text)
#         else:
#             print(text)
#
#     elif command == "Switch":
#         old_str = to_do_info[1]
#         new_str = to_do_info[2]
#
#         if old_str in text:
#             current_text = text.replace(old_str, new_str)
#             text = current_text
#             print(text)
#         else:
#             print(text)
#
# print(f"Ready for world tour! Planned stops: {text}")