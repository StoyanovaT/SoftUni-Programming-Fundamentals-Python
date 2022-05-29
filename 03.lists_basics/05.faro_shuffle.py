starting_list = input().split(" ")
shuffles = int(input())

first_char = starting_list[0]
last_char = starting_list[-1]

shuffled_deck = starting_list

first_list = []
second_list = []

half_of_deck = int(len(starting_list) / 2)

for _ in range(shuffles):
    first_list = shuffled_deck[1:half_of_deck]
    second_list = shuffled_deck[half_of_deck:-1]
    shuffled_deck = []
    for num in range(len(second_list)):
        if num == 0:
            shuffled_deck.append(starting_list[0])
        shuffled_deck.append(second_list[num])
        shuffled_deck.append(first_list[num])
        if num == (len(second_list) - 1):
            shuffled_deck.append(starting_list[-1])

print(shuffled_deck)
