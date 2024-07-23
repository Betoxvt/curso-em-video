# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
c = 0
s = 0
print('Calcular a soma entre vários números')
print('Digite números inteiros ou 999 para parar')
while n != 999:
    n = int(input('>>>> '))
    if n != 999:
        s += n
        c += 1
print(f'{c} números digitados e a soma entre eles da {s}.')
