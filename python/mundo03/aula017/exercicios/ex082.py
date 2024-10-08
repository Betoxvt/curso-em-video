# Dividing values in multiple lists
# Create a program thar will read multiple numbers and place them in a numbers_list.
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

# Teacher's solution
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')