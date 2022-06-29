text = input()
letters = ""
last_letter = ""
for let in text:
    if let not in letters:
        letters += let
        last_letter = let
    else:
        if let != last_letter:
            letters += let
            last_letter = let

print(letters)
