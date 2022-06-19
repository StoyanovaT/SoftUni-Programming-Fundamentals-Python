contests_passes_dict = {}
students_submissions_data = {}
text = input()
valid = False


while True:
    if text == "end of contests":
        break

    (contest, password) = text.split(":")
    contests_passes_dict[contest] = password

    text = input()

submission = input()
while True:
    if submission == "end of submissions":
        break

    (st_contest, st_password, username, points) = submission.split("=>")

    if st_contest in contests_passes_dict.keys() and st_password == contests_passes_dict[st_contest]:
        if username not in students_submissions_data:
            students_submissions_data[username] = {}
        if st_contest not in students_submissions_data[username]:
            students_submissions_data[username][st_contest] = int(points)
        else:
            if students_submissions_data[username][st_contest] < int(points):
                students_submissions_data[username][st_contest] = int(points)

    submission = input()

best_student = ""
best_points = 0

for student in students_submissions_data.keys():
    tot_points = sum(students_submissions_data[student].values())
    if tot_points > best_points:
        best_points = tot_points
        best_student = student

print(f"Best candidate is {best_student} with total {best_points} points.")
print("Ranking:")
for student in sorted(students_submissions_data.keys()):
    print(student)
    for (contest, points) in sorted(students_submissions_data[student].items(), key=lambda cp: -cp[1]):
        print(f"#  {contest} -> {points}")




# na lektor
# contest_data = input()
# contests_dict = dict()
#
# while contest_data != "end of contests":
#     (contest, password) = contest_data.split(":")
#     contests_dict[contest] = password
#     contest_data = input()
#
# submission_data = input()
# users_dict = {}
#
# while submission_data != "end of submissions":
#     (contest, password, user, points) = submission_data.split("=>")
#
#     if contest in contests_dict and contests_dict[contest] == password:
#         if user not in users_dict:
#             users_dict[user] = {}
#
#         if contest not in users_dict[user]:
#             users_dict[user][contest] = int(points)
#         else:
#             if users_dict[user][contest] < int(points):
#                 users_dict[user][contest] = int(points)
#
#     submission_data = input()
#
# best_user = ""
# best_points = 0
#
# for user in users_dict.keys():
#     total_points = sum(users_dict[user].values())
#     if total_points > best_points:
#         best_points = total_points
#         best_user = user
#
#
# print(f"Best candidate is {best_user} with total {best_points} points.")
# print("Ranking:")
# for user in sorted(users_dict.keys()):
#     print(user)
#     for (contest, points) in sorted(users_dict[user].items(), key= lambda cp: -cp[1]):
#         print(f"#  {contest} -> {points}")