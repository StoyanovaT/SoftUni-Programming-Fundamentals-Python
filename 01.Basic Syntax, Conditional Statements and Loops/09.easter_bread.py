budget = float(input())
price_1kg_flour = float(input())
colored_eggs = 0
breads_made = 0

price_1pack_eggs = price_1kg_flour * 0.75
price_250ml_milk = (price_1kg_flour + (price_1kg_flour * 0.25)) / 4

price_of_one_bread = price_1kg_flour + price_1pack_eggs + price_250ml_milk

while True:
    if budget >= price_of_one_bread:
        breads_made += 1
        budget -= price_of_one_bread
        colored_eggs += 3
        if breads_made % 3 == 0:
            colored_eggs -= breads_made - 2
    else:
        break

print(f"You made {breads_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
