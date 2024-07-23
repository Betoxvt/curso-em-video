# SEQUÊNCIA DE FIBONACCI
# Escreva um programa que leia um número inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
c = 1
e = int(input('Digite o nº de elementos: '))
na = 0
nb = 1
nc = 0
print(f'Os {e} primeiros elementos da sequência de Fibonacci são:')
print(0, end=' → ')
while c < e - 1:
    print(nb, end=' → ')
    c += 1
    na = nb
    nb = nc + na
    nc = nb - nc
print(nb)
