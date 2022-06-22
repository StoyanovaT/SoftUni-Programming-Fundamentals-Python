students_points_dict = {}
language_submissions_count_dict = {}


while True:
    student_information = input()

    if student_information == "exam finished":
        break

    student_info = student_information.split("-")
    if student_info[1] != "banned":
        name = student_info[0]
        language = student_info[1]
        points = int(student_info[2])

        if name not in students_points_dict.keys():
            students_points_dict[name] = points
        else:
            if students_points_dict[name] < points:
                students_points_dict[name] = points

        if language not in language_submissions_count_dict.keys():
            language_submissions_count_dict[language] = 1
        else:
            language_submissions_count_dict[language] += 1

    else:
        banned_name = student_info[0]
        del students_points_dict[banned_name]

print("Results:")
for (name, points) in students_points_dict.items():
    print(f"{name} | {points}")

print("Submissions:")
for (language, subm_count) in language_submissions_count_dict.items():
    print(f"{language} - {subm_count}")
