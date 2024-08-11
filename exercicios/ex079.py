# Unique values in a numbers_list
# Create a program where the user can enter multiple numeric values and register them in a numbers_list.
# If the number already exists in it, it won't get added.
# At the end, show all the unique values entered, in ascending order.
unique_numbers = list()
while True:
    number = int(input('Enter a value: '))
    if number not in unique_numbers:
        unique_numbers.append(number)
        print('Value registered with success.')
    else:
        print('Value already registered.')
    more = ' '
    while more not in 'YN':
        more = str(input('Do you wish to continue? [Y/N] ')).strip().upper()[0]
    if more == 'N':
        break
print('—'*40)
print(f'You entered the values: {sorted(unique_numbers)}')
