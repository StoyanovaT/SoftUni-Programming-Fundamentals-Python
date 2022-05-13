string = input().lower()

words = string.count("sand")
words += string.count("water")
words += string.count("fish")
words += string.count("sun")

print(words)
