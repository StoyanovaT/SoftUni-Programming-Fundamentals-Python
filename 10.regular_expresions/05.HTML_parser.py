import re
text = input()

regex_title = r"<title>([^<>]*)<\/title>"

title = re.findall(regex_title, text)
title = ''.join(title)
print(f"Title: {title}")

regex_content = r"<body>.*<\/body>"
content = re.findall(regex_content, text)
content = "".join(content)

pattern = r">([^><]*)<"

body = re.findall(pattern, content)

body = ''.join(body)
body = body.replace('\\n', '')
print(f"Content: {body}")


