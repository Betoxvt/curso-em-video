# Employee registration in Python
# Create a program that reads name, year of birth and work record booklet (number)
# then register them (with age) in a dictionary.
# If WRB is not equal to 0, the dictionary will also receive the year of contract and salary.
# Calculate and add, besides the age, how old the person will be when retires (I assume 35 years of contribution).
from datetime import date
employee = dict()
employee['Name'] = input('Name: ')
birth = int(input('Year of birth: [yyyy] '))
employee['WRB'] = int(input('Work record booklet number: ([0] if none) '))
employee['Age'] = date.today().year - birth
if employee['WRB'] != 0:
    employee['Contract'] = int(input('Year of contract [yyyy]: '))
    employee['Salary'] = float(input('Salary: $ '))
    employee['Age_of_Retirement'] = employee['Age'] + ((employee['Contract'] + 35) - date.today().year)
print('—'*30)
for k, v in employee.items():
    print(f'{k}: {v}')
