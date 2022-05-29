numbers_list = input().split(", ")
beggars = int(input())
earned_sum = 0
earned_list = []

for i in range(beggars):
    for j in range(i, len(numbers_list), beggars):
        earned_sum += int(numbers_list[j])
    earned_list.append(earned_sum)
    earned_sum = 0

print(earned_list)
