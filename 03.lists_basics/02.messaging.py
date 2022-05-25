numbers = input().split(" ")
text = str(input())
text_list = list(text)
nums_sum = 0

for i in numbers:
    for j in i:
        nums_sum += int(j)
    if len(text_list) < nums_sum:
        nums_sum -= len(text_list)
    letter = text_list[nums_sum]
    text_list.pop(nums_sum)
    nums_sum = 0

    print(letter, end="")
