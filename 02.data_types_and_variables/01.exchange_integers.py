a = int(input())
b = int(input())
print("Before:", f"a = {a}",  f"b = {b}", sep="\n")

a, b = b, a

print("After:", f"a = {a}",  f"b = {b}", sep="\n")
