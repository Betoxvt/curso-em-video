# Extracting data from a numbers_list
# Create a program that reads multiple numbers and place them in a numbers_list.
# After that, show:
# A) How many numbers where entered.
# B) The numbers_list of values, sorted in descending order.
# C) If the value 5 was entered and is or isn't in the numbers_list.
numbers = list()
while True:
    numbers.append(int(input('Enter value: ')))
    more = ' '
    while more not in 'YN':
        more = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if more == "N":
        break
print('—' * 50)
print(f'The list you entered is {numbers}')
print(f'A) You entered {len(numbers)} numbers')
numbers.sort(reverse=True)
print(f'B) The list in descending order is {numbers}')
if 5 in numbers:
    print(f'C) The number 5 is in the list')
else:
    print(f'C) The number 5 is not in the list')

# Teacher's solution
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
