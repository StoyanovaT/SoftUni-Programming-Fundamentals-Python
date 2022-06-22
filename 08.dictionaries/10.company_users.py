
company_info = {}

while True:
    info = input()

    if info == "End":
        break

    (company, employee_id) = info.split(" -> ")

    if company not in company_info:
        company_info[company] = [employee_id]
    else:
        if employee_id not in company_info[company]:
            company_info[company].append(employee_id)


for key in company_info.keys():
    print(f"{key}")
    for id in company_info[key]:
        print(f"-- {id}")
