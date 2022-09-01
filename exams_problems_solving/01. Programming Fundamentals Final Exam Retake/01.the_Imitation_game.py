text = input()

while True:
    to_do = input().split("|")

    if to_do[0] == "Decode":
        break

    if to_do[0] == "Move":
        num_of_letters = int(to_do[1])
        text = text[num_of_letters:] + text[:num_of_letters]

    elif to_do[0] == "Insert":
        index = int(to_do[1])
        value = to_do[2]
        text = text[:index] + value + text[index:]

    elif to_do[0] == "ChangeAll":
        substring= to_do[1]
        replacement = to_do[2]
        text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")
