n = int(input())
previous_bracket = ")"
is_balanced = True
for _ in range(n):
    data = input()
    if data == chr(40) or data == chr(41):
        if not previous_bracket == data:
            previous_bracket = data
        else:
            is_balanced = False
            print("UNBALANCED")
            break

if is_balanced:
    print("BALANCED")