lines = int(input())
capacity = 255
ltrs_in_tank = 0

for i in range(lines):
    ltrs_water = int(input())
    if (capacity - ltrs_in_tank) >= ltrs_water:
        ltrs_in_tank += ltrs_water
    else:
        print("Insufficient capacity!")
print(ltrs_in_tank)

# Решение на Марио
# number_of_lines = int(input())
# capacity = 0
#
# for _ in range(number_of_lines):
#     liters_of_water = int(input())
#
#     if liters_of_water + capacity <= 255:
#         capacity += liters_of_water
#         continue
#
#     print("Insufficient capacity!")
# print(capacity)