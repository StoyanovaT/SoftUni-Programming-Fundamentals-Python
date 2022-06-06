def validator(password):
    valid = True
    if 6 > len(password) or len(password) > 10:
        valid = False
        print("Password must be between 6 and 10 characters")

    for i in password:
        if ord(i) in range(48, 58) or ord(i) in range(65, 91) or ord(i) in range(97, 123):
            continue
        else:
            valid = False
            print("Password must consist only of letters and digits")
            break

    digits_count = 0
    for j in password:
        if ord(j) in range(48, 58):
            digits_count += 1
    if digits_count < 2:
        valid = False
        print("Password must have at least 2 digits")

    if valid:
        print("Password is valid")


password_entered = input()
validator(password_entered)
