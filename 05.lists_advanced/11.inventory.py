def collect_func(data, item):
    if item not in data:
        data.append(item)

    return data


def drop_func(data, item):
    if item in data:
        data.remove(item)

    return data


def combine_items_func(data, items):
    items = items.split(':')
    old_element = items[0]
    new_element = items[1]

    if old_element in data:
        index_old_element = data.index(old_element)
        data.insert(index_old_element + 1, new_element)

    return data


def renew_func(data, item):
    if item in data:
        data.remove(item)
        data.append(item)

    return data


def inventory(data):
    while True:
        command = input().split(' - ')

        if command[0] == 'Craft!':
            print(', '.join(data))
            break

        current_command = command[0]
        item = command[1]

        if current_command == 'Collect':
            data = collect_func(data, item)
        elif current_command == 'Drop':
            data = drop_func(data, item)
        elif current_command == 'Combine Items':
            data = combine_items_func(data, item)
        elif current_command == 'Renew':
            data = renew_func(data, item)


info = input().split(', ')
inventory(info)

# journal = input().split(", ")
#
# line = input().split(" - ")
# while "Craft!" not in line:
#     if line[0] == "Combine Items":
#         combine = line[1].split(":")
#         old_item = combine[0]
#         new_item = combine[1]
#         if old_item in journal:
#             index_old_item = journal.index(old_item)
#             journal.insert(index_old_item + 1, new_item)
#     else:
#         command = line[0]
#         item = line[1]
#         if command == "Collect":
#             if item not in journal:
#                 journal.append(item)
#
#         elif command == "Drop":
#             if item in journal:
#                 journal.remove(item)
#
#         elif command == "Renew":
#             if item in journal:
#                 journal.remove(item)
#                 journal.append(item)
#     line = input().split(" - ")
#
# inventory = ", ".join(journal)
# print(inventory)