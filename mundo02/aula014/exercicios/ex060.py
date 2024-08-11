# CALCULO DO FATORIAL
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Tente com while e com for
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
print('Este programa mostra o fatorial de um número')
n = int(input('Insira o valor: '))
fat = 1

# Usando while
if n > 0:
    print(f'{n}! =', end=' ')
    while n > 0:
        print(f'{n}', end='')
        print(' x ' if n > 1 else ' = ', end='')
        fat *= n
        n -= 1
    print(f'{fat}')
elif n == 0:
    print('0! = 1')
elif n < 0:
    print('Não há fatorial de números negativos')
'''
# Usando for
if n > 0:
    print(f'{n}! =', end=' ')
    for n in range(n, 0, -1):
        print(f'{n}', end='')
        print(' x ' if n > 1 else ' = ', end='')
        fat *= n
    print(fat)
elif n == 0:
    print('0! = 1')
elif n < 0:
    print('Não há fatorial de números negativos')
'''
