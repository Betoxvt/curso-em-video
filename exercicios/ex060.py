# CALCULO DO FATORIAL
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Tente com while e com for
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
print('Este programa mostra o fatorial de um número')
n = int(input('Insira o valor: '))
fat = n

# Usando while
if n > 1:
    print(f'{n}! =', end=' ')
    while n != 1:
        print(f'{n}', end=' X ')
        fat = fat * (n-1)
        n += -1
    print(f'1 = {fat}')
elif n == 1:
    print('1! = 1')
elif n == 0:
    print('0! = 1')
elif n < 0:
    print('Não há fatorial de números negativos')

# Usando for
'''
if n > 1:
    print(f'{n}! =', end=' ')
    for n in range(n, 1, -1):
        if n > 1:
            fat = fat*(n-1)
            print(f'{n}', end=' X ')
    print('1 = {}'.format(fat))
elif n == 1:
    print('1! = 1')
elif n == 0:
    print('0! = 1')
elif n < 0:
    print('Não há fatorial de números negativos')
'''
