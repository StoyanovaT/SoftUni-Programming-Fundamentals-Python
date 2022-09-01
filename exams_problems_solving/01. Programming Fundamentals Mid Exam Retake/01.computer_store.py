tot_price_no_taxes = []
tot_price_with_taxes = 0
tot_taxes = 0
tot_discount = 0
special = False

while True:
    price_no_tax = input()
    if price_no_tax == "special" or price_no_tax == "regular":
        if price_no_tax == "special":
            special = True
        break

    else:
        price_no_tax = float(price_no_tax)
        if price_no_tax < 0:
            print("Invalid price!")
        else:
            tot_price_no_taxes.append(price_no_tax)

tot_taxes = sum(tot_price_no_taxes) * 0.20
tot_price_with_taxes = float(sum(tot_price_no_taxes)) + tot_taxes

if special:
    tot_price_with_taxes -= tot_price_with_taxes * 0.10

if tot_price_with_taxes == 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum(tot_price_no_taxes):.2f}$")
    print(f"Taxes: {tot_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {tot_price_with_taxes:.2f}$")
