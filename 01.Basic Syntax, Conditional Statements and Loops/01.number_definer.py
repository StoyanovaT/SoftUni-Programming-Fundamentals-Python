n = float(input())

if n == 0:
    print("zero")
elif n > 0:
    if n > 1000000:
        print("large positive")
    elif n < 1:
        print("small positive")
    else:
        print("positive")
elif n < 0:
    if n < - 1000000:
        print("large negative")
    elif n > -1:
        print("small negative")
    else:
        print("negative")