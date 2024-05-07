student = {}

student['name'] = input('Name: ').title()
student['average'] = float(input(f'Average of {student["name"].title()}: '))

if student['average'] < 5:
    student['status'] = 'Reproved'
elif student['average'] >= 5 and student['average'] <= 10:
    student['status'] = 'Approved'

for k, v in student.items():
    print(f'The {k} is {v}.')