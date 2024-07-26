# Análise de dados em uma tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
tup = (int(input('Enter the first number: ')),
       int(input('Enter the second number: ')),
       int(input('Enter the third number: ')),
       int(input('Enter the fourth number: ')))
print(f'You entered {tup}')
even = ''
print(f'A) "9" appeared {tup.count(9)} times')
if 3 in tup:
    print(f'B) First "3" appeared at position {tup.index(3) + 1}')
else:
    print('B) "3" is not present in the Tuple')
for n in tup:
    if n % 2 == 0:
        even += str(f'"{n}", ')
if len(even) == 0:
    print('C) There are no even numbers')
else:
    even = even[:-2]
    print(f'C) The even numbers are: {even[::-1].replace(',', ' and'[::-1], 1)[::-1]}')
