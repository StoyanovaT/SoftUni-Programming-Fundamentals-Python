net_price = 0

while True:
    parts = input()
    if parts == "special" or parts == "regular":
        break
    elif float(parts) < 0:
        print("Invalid price!")
        continue
    net_price += float(parts)


taxes = net_price * 0.20
tot_price_with_tax = net_price + taxes

if parts == "special":
    discount = tot_price_with_tax * 0.10
    tot_price_with_tax -= discount

if tot_price_with_tax == 0:
    print("Invalid order!" )
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {tot_price_with_tax:.2f}$")

# line = input()
# net_price = 0
#
# while line != "special" and line != "regular":
#     current_price = float(line)
#
#     if current_price > 0:
#         net_price += current_price
#     else:
#         print("Invalid price!")
#
#     line = input()
#
# if net_price <= 0:
#     print("Invalid order!")
# else:
#     taxes = net_price * 0.2
#     final_price = net_price + taxes
#
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {net_price:.2f}$")
#     print(f"Taxes: {taxes:.2f}$")
#     print("-----------")
#
#     if line == "special":
#         final_price = final_price * 0.9
#
#     print(f"Total price: {final_price:.2f}$")