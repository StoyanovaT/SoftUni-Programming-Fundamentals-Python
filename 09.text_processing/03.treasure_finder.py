import re
key_raw = input().split()
keys = [int(num) for num in key_raw]

while True:
    text = input()

    if text == "find":
        break
    index = 0
    decrypted = ""
    for i in text:
        decrypted += chr(ord(i) - keys[index])
        if index == len(keys) - 1:
            index = 0
        else:
            index += 1

    regex = r".*\&([A-Za-z]+)\&.*\<([A-Za-z0-9]+)\>.*"
    treasure = re.finditer(regex, decrypted)
    for match in treasure:
        print(f"Found {match.group(1)} at {match.group(2)}")
