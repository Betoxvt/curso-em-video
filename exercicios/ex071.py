# Simulador de caixa eletrônico
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
n50 = n20 = n10 = 0
print('='*30)
print('Bem vindo ao caixa eletrônico!')
print('='*30)
print('Notas disponíveis:'
      '\n[R$50] [R$20] [R$10] [R$1]')
print('='*30)
print('Quanto gostaria de sacar?')
saque = int(input('>>>>  R$'))
print('='*30)

n1 = saque
while n1 >= 50:
    n1 -= 50
    n50 += 1
while n1 >= 20:
    n1 -= 20
    n20 += 1
while n1 >= 10:
    n1 -= 10
    n10 += 1
print('Notas  |  Qntd.')
if n50 > 0:
    print(f'[R$50]: {n50:>5}')
if n20 > 0:
    print(f'[R$20]: {n20:>5}')
if n10 > 0:
    print(f'[R$10]: {n10:>5}')
if saque > 0:
    print(f'[R$1] : {n1:>5}')
print(f'Total :  R${saque:.2f}')
print('='*30)

'''
n50 = saque // 50
saque = saque - n50 * 50
n20 = saque // 20
saque = saque - n20 * 20
n10 = saque // 10
saque = saque - n10 * 10
print('Notas  |  Qntd.')
if n50 > 0:
    print(f'[R$50]: {n50:>5}')
if n20 > 0:
    print(f'[R$20]: {n20:>5}')
if n10 > 0:
    print(f'[R$10]: {n10:>5}')
if saque > 0:
    print(f'[R$1] : {saque:>5}')
print('='*30)
'''
