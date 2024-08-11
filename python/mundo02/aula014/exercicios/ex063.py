# SEQUÊNCIA DE FIBONACCI
# Escreva um programa que leia um número inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

print('-=-' * 10)
e = int(input('Digite o nº de elementos: ').center(30))
print('-=-' * 10)
c = 1
na = 0
nb = 1
nc = 0
if e == 0:
    print('Ok nenhum elemento então')
if e == 1:
    print('O primeiro elemento da sequência de Fibonacci é:')
    print('~~' * 30,
          '\n0')
if e > 1:
    print(f'A Sequência de Fibonacci com {e} elementos é:')
    print('~~' * 30)
    print(0, end=' → ')
    while c < e - 1:
        print(nb, end=' → ')
        c += 1
        na = nb
        nb = nc + na
        nc = nb - nc
    print(nb)
if e < 0:
    (print('Por favor use números inteiros e positivos de preferência'))
print('~~' * 30)
print('FIM')
