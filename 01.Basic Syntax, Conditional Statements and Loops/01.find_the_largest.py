number = input()
largest_num = []
new_num = ""

for i in number:
    largest_num.append(i)
largest_num.sort(reverse=True)
for l in range(len(largest_num)):
    new_num += largest_num[l]

print(new_num)