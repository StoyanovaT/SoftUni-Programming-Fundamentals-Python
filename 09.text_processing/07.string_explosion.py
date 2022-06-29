text = input()
new_text = ""
strength = 0
for index in range(len(text)):
    if text[index] == ">":
        new_text += text[index]

    else:
        if text[index].isnumeric():
            strength += int(text[index])
        if strength > 0:
            strength -= 1
        elif strength == 0:
            new_text += text[index]

print(new_text)
