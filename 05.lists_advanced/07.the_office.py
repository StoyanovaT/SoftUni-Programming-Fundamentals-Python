employees = input().split(" ")
employees = map(int, employees)
factor = int(input())

employees = [num * factor for num in employees]
average = sum(employees) / len(employees)
happy_employees = [happy for happy in employees if happy >= average]

if len(happy_employees) >= len(employees) /2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")
