# products_dict = {}
#
# while True:
#     info = input()
#
#     if info == "buy":
#         break
#
#     info = info.split(" ")
#     product = info[0]
#     price = float(info[1])
#     quantity = int(info[2])
#
#     if product in products_dict:
#         products_dict[product] = [price, (quantity + products_dict[product][1])]
#     else:
#         products_dict[product] = [price, quantity]
#
# for i in products_dict.keys():
#     total_price = products_dict[i][0] * products_dict[i][1]
#     print(f"{i} -> {total_price:.2f}")

# решение на Марио с функции:
def orders_func(orders_dict, command):
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product in orders_dict:
        orders_dict[product] = [price, (quantity + orders_dict[product][1])]
    else:
        orders_dict[product] = [price, quantity]

    return orders_dict


def orders():
    orders_dict = {}

    while True:
        command = input()

        if command == "buy":
            break

        command = command.split(" ")
        orders_dict = orders_func(orders_dict, command)

    for k in orders_dict:
        total_sum = orders_dict[k][0] * orders_dict[k][1]
        print(f"{k} -> {total_sum:.2f}")


orders()
