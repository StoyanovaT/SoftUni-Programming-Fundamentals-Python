def palindrome(num):
    for i in numbers:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palindrome(numbers)
