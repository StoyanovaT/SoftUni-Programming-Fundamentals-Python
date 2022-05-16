number_of_orders = int(input())
tot_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price = price_per_capsule * capsules_count * days
    tot_price += price

    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${tot_price:.2f}")