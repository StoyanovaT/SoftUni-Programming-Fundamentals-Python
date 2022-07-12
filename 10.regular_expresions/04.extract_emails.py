import re
text = input()

user_pattern = r"( |^)[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*"
host_pattern = r"[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"

pattern = rf"{user_pattern}@{host_pattern}"

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])

# neshto se chupi
# import re
# text = input()
#
# regex = r"(^|(?<=\s|^)([a-z\d]+([._-])?[a-z\d]+)@([a-z]+)([\.-])?[a-z]+\.[a-z]+)"
#
# matches = re.finditer(regex, text)
# for match in matches:
#
#     print(match)

