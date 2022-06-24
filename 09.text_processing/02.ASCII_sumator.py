start = ord(input())
end = ord(input())
text = input()

total = [ord(num) for num in text if start < ord(num) < end]

print(sum(total))
