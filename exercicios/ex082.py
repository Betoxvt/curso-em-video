# Dividing values in multiple lists
# Create a program thar will read multiple numbers and place them in a list.
# After that, create two extra lists that will content only even values and odd values entered, respectively.
# At the end, show the content of the three generated lists.
numbers = list()
while True:
    numbers.append(int(input('Enter value: ')))
    more = ' '
    while more not in 'YN':
        more = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if more == 'N':
        break
print('—'*36)
print(f'The full list is {numbers}')
even_numbers = list()
odd_numbers = list()
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
print(f'The even numbers list is {even_numbers}')
print(f'The odd numbers list is {odd_numbers}')
