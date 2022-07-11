# import re
#
# text = input()
#
# regex = r"(?<=\b_{1})[A-Za-z0-9]+\b"
#
# matches = re.findall(regex, text)
#
# print(",".join(matches))

# mario:

import re

data = input()

pattern = r"\b_[a-zA-Z0-9]+\b"

result = re.findall(pattern, data)

words_list = []

for word in result:
    words_list.append(word[1:])

print(",".join(words_list))
