key = int(input())
lines = int(input())
message = []

for i in range(lines):
    letter = str(input())
    true_letter = chr(ord(letter) + key)
    print(true_letter, end="")
    