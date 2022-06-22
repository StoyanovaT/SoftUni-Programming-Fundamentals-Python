courses_info = {}

while True:
    info = input()

    if info == "end":
        break

    (course_name, student_name) = info.split(" : ")
    if course_name not in courses_info:
        courses_info[course_name] = [student_name]
    else:
        courses_info[course_name].append(student_name)


for key in courses_info.keys():
    print(f"{key}: {len(courses_info[key])}")
    for name in courses_info[key]:
        print(f"-- {name}")
