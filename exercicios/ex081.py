# Extracting data from a list
# Create a program that reads multiple numbers and place them in a list.
# After that, show:
# A) How many numbers where entered.
# B) The list of values, sorted in descending order.
# C) If the value 5 was entered and is or isn't in the list.
numbers = list()
while True:
    numbers.append(int(input('Enter value: ')))
    more = ' '
    while more not in 'YN':
        more = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if more == "N":
        break
print(f'The list you entered is {numbers}')
print(f'A) You entered {len(numbers)} numbers')
numbers.sort(reverse=True)
print(f'B) The list in descending order is {numbers}')
if 5 in numbers:
    print(f'C) The number 5 is in the list')
else:
    print(f'C) The number 5 is not in the list')
