animals = input().split()

list_animals = animals
list_animals.reverse()

for position, animal in enumerate(list_animals):
    if animal == "wolf" or animal == "wolf,":
        if position == 0:
            print("Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {position}! You are about to be eaten by a wolf!" )
