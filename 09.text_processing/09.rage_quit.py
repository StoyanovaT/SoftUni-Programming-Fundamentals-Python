text = input()
final_text = ""
text_to_repeat = ""
times_to_repeat = ""

for i in range(len(text)):
    if not text[i].isnumeric():
        text_to_repeat += text[i]
    else:
        times_to_repeat += text[i]
        if len(text) - i != 1:
            if text[i + 1].isnumeric():
                continue
        final_text += text_to_repeat.upper() * int(times_to_repeat)
        text_to_repeat = ""
        times_to_repeat = ""

final_text_set = set(final_text)
print(f"Unique symbols used: {len(final_text_set)}")
print(final_text)
