number_of_pieces = int(input())
pieces_dict = {}
for _ in range(number_of_pieces):
    pieces_raw = input().split("|")

    pieces_dict[pieces_raw[0]] = []
    pieces_dict[pieces_raw[0]].append(pieces_raw[1])
    pieces_dict[pieces_raw[0]].append(pieces_raw[2])

while True:
    info = input().split("|")

    if info[0] == "Stop":
        break

    elif info[0] == "Add":
        piece = info[1]
        composer = info[2]
        key = info[3]

        if piece in pieces_dict.keys():
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = []
            pieces_dict[piece].append(composer)
            pieces_dict[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif info[0] == "Remove":
        piece = info[1]
        if piece in pieces_dict.keys():
            pieces_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif info[0] == "ChangeKey":
        piece = info[1]
        new_key = info[2]

        if piece in pieces_dict.keys():
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for name in pieces_dict.keys():
    print(f"{name} -> Composer: {pieces_dict[name][0]}, Key: {pieces_dict[name][1]}")
