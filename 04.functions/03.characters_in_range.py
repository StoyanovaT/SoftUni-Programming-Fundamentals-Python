def characters_between(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


start, end = input(), input()

characters_between(start, end)
