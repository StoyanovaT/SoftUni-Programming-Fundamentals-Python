import re
number_of_strings = int(input())

for _ in range(number_of_strings):
    text = input()

    regex_name = r"@[A-Za-z]+\|"
    regex_age = r"\#\d+\*"

    match_name = re.findall(regex_name, text)
    match_age = re.findall(regex_age, text)
    name = ''.join(match_name)
    name = name[1:-1]
    age = ''.join(match_age)
    age = age[1:-1]

    print(f"{name} is {age} years old.")
