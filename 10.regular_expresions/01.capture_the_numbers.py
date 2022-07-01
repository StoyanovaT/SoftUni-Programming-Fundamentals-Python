import re

regex = r"(\d+)"

while True:
    text = input()
    if not text:
        break

    matches = re.findall(regex, text)

    if len(matches) > 0:
        print(" ".join(matches), end=" ")
