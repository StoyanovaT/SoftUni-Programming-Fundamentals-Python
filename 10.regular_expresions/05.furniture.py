import re

furniture_names = list()
total_price = 0

while True:
    text = input()

    if text == "Purchase":
        break

    pattern = r"(>>(?P<furniture>[a-zA-Z]+)<<(?P<price>[0-9]+(\.[0-9]+)*)!(?P<quantity>[0-9]+\b))"

    matches = re.finditer(pattern, text)
    for match in matches:
        furniture = match.group("furniture")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        furniture_names.append(furniture)
        total_price += quantity * price

print("Bought furniture:")

for i in furniture_names:
    print(i)

print(f"Total money spend: {total_price:.2f}")

# Mario
# import re
#
#
# def furniture_info():
#     pattern = r"([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)"
#     spend_money = 0
#     product_list = []
#
#     while True:
#         data = input()
#
#         if data == "Purchase":
#             break
#
#         result = re.match(pattern, data)
#
#         if result is not None:
#             product = result[1]
#             price = float(result[2])
#             quantity = float(result[3])
#             spend_money += price * quantity
#             product_list.append(product)
#
#     print("Bought furniture:")
#
#     if spend_money > 0:
#         print("\n".join(product_list))
#     print(f"Total money spend: {spend_money:.2f}")
#
#
# furniture_info()
