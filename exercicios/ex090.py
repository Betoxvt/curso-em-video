# Dictionary
# Create a program that reads name and average from a student, saving also his situation in a dictionary.
# At the end, show the content of the structure on screen.
student = {'Name': input('Name: ')}
student['Average'] = float(input(f'{student["Name"]} Average: '))
if student['Average'] >= 7:
    student['Situation'] = 'Passed'
elif 5 <= student['Average'] < 7:
    student['Situation'] = 'On Probation'
else:
    student['Situation'] = 'Failed'

for k, v in student.items():
    print(k, 'is', v)
