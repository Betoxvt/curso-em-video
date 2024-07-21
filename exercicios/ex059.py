# CRIANDO UM MENU DE OPÇÕES
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
print('Insira os números para o programa.')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sleep(0.5)
opt = 0
while opt != 5:
    print('-------- MENU ---------')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do Programa')
    print('-----------------------')
    sleep(0.5)
    opt = int(input('Escolha uma das opções: '))
    if opt == 1:
        sleep(0.5)
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
        sleep(3)
    if opt == 2:
        sleep(0.5)
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
        sleep(3)
    if opt == 3:
        sleep(0.5)
        if n1 == n2:
            print('Os números {} são iguais'.format(n1))
            sleep(3)
        if n1 > n2:
            print('{} é o MAIOR.'.format(n1))
            sleep(3)
        if n2 > n1:
            print('{} é o MAIOR.'.format(n2))
            sleep(3)
    if opt == 4:
        sleep(0.5)
        print('Inserir novos números para o programa.')
        sleep(0.5)
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(0.5)
sleep(0.5)
print('Fim do programa')
