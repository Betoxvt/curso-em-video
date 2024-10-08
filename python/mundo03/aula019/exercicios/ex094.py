# Appending dictionaries to a numbers_list
# Create a program that reads Name, Gender and Age of multiple subjects, storing the data of each person
# in a dictionary and all of them in a numbers_list. Finally, print:
# A) How many people registered
# B) Age average
# C) Females numbers_list
# D) Above average age numbers_list
data = list()
agesum = 0
while True:
    subj = {'Name': input('Name: ').strip().title(),
            'Age': int(input('Age: '))}
    agesum += subj['Age']
    while True:
        subj['Gender'] = input('Gender: [M/F] ').strip().upper()[0]
        if subj['Gender'] in 'MF':
            break
        print('Gender must be either "M" or "F".')
    data.append(subj.copy())
    while True:
        ans = input('Wish to continue? [Y/N] ').strip().upper()[0]
        if ans in 'YN':
            break
        print('You must enter either Y or N.')
    if ans == 'N':
        break
print('—' * 46)
print(f'A) Total of {len(data)} people records')
average = agesum / len(data)
print(f'B) The age average is {average:.0f}')
print(f'C) The females registered were: ', end='')
for i in range(len(data)):
    if data[i]['Gender'] == 'F':
        print(f'"{data[i]["Name"]}" ', end='')
print(f'\nD) List of people above the average age:')
for p in data:
    if p['Age'] > average:
        print('    → ', end='')
        for k, v in p.items():
            print(f'{k}: {v}; ', end='')
        print()
print()
print(' END OF PROGRAM '.center(45, "—"))
