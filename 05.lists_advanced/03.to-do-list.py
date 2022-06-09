to_do_list = ["" for i in range(11)]


command = input()

while command != "End":
    to_do_note = command.split("-")
    priority = int(to_do_note[0])
    task = to_do_note[1]
    to_do_list[priority] = task

    command = input()

final_to_do_list = [task for task in to_do_list if task != ""]
print(final_to_do_list)
