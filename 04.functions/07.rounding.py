def convert_list_to_round(base_list):
    final_list = list()
    for n in base_list:
        final_n = round(float(n))
        final_list.append(final_n)
    return final_list


input_list= input().split()

print(convert_list_to_round(input_list))
#
# def rounding():
#     rounded_list = []
#     for num in numbers:
#         current_num = round(float(num))
#         rounded_list.append(current_num)
#     return rounded_list
#
#
# numbers = input().split(" ")
#
# print(rounding())