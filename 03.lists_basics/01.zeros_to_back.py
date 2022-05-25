list = input().split(", ")
list_1 = []
list_2 = []

for i in list:
    if int(i) == 0:
        list_2.append(int(i))

    else:
        list_1.append(int(i))

print(list_1 + list_2)