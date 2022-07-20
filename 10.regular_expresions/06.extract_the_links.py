import re

while True:
    text = input()
    if not text:
        break

    regex = r"(?P<link>www\.[a-zA-Z0-9\-]+(\.[a-z]+)+)"

    matches = re.finditer(regex, text)

    for match in matches:
        link = match.group("link")
        print(link)