vowels = ["a", "o", "u", "e", "i"]
text = input()
no_vowels = [ch for ch in text if ch not in vowels]

# заместваме това с горния ред:
# for ch in text:
#     if ch not in vowels:
#         no_vowels.append(ch)

print("".join(no_vowels))