def phone_book_information(number_of_lines, phone_book):
    for x in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")

    return True


def phone_book_info():
    phone_book = {}
    condition = False

    while True:
        contact_information = input().split("-")

        if contact_information[0].isdigit():
            condition = phone_book_information(int(contact_information[0]), phone_book)
        else:
            phone_book[contact_information[0]] = contact_information[1]

        if condition:
            break


phone_book_info()

# мое решение в Judge дава 80/100, да му потърся грешката:
# phone_book = {}
#
# while True:
#     name_number = input().split("-")
#
#     if name_number[0].isdigit():
#         break
#
#     (name, number) = name_number
#
#     if name not in phone_book.keys():
#         phone_book[name] = number
#     else:
#         phone_book[name] = number
#
# number_of_lines = int(name_number[0])
#
# for i in range(number_of_lines):
#     searched_name = input()
#     for key in phone_book.keys():
#         if key == searched_name:
#             print(f"{searched_name} -> {phone_book[searched_name]}")
#         if searched_name not in phone_book.keys():
#             print(f"Contact {searched_name} does not exist.")
#             break
