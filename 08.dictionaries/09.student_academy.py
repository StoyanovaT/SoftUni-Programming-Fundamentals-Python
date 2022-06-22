pairs_of_rows = int(input())
students_dict = {}
for _ in range(pairs_of_rows):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_dict.keys():
        students_dict[student_name] = [student_grade]

    else:
        students_dict[student_name].append(student_grade)

for key in students_dict.keys():
    average_grade = sum(students_dict[key]) / len(students_dict[key])
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")
