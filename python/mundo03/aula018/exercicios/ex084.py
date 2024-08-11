# Nested numbers_list and data analysis
# Create a program that reads name and weight os multiple persons, saving it all in a numbers_list.
# At the end, print:
# A) How many persons registered.
# B) A numbers_list with the heaviest persons.
# C) A numbers_list with the lightest persons.
Persons = []
while True:
    Person = [str(input('Name: ')), float(input('Weight: '))]
    Persons.append(Person[:])
    Person.clear()

    Continue = str(input('Continue? [Y/N] ')).upper().strip()[0]
    while Continue not in 'YN':
        Continue = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if Continue == 'N':
        break

heaviest = lightest = Persons[0][1]
for p in Persons:
    weight = p[1]
    if weight > heaviest:
        heaviest = weight
    if weight < lightest:
        lightest = weight

print('—'*50)
print(f'A) {len(Persons)} persons registered.')

print(f'B) The heaviest weight is {heaviest}Kg. Belonging to', end=' ')
for p in Persons:
    if p[1] == heaviest:
        print(f'[{p[0]}] ', end='')

print(f'\nC) The lightest weight is {lightest}Kg. Belonging to', end=' ')
for p in Persons:
    if p[1] == lightest:
        print(f'[{p[0]}] ', end='')
