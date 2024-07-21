# CRIANDO UM MENU DE OPÇÕES
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opt = 0
while opt != 5:
    print('-------- MENU ---------')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do Programa')
    print('-----------------------')
    opt = int(input('Escolha: '))
    if opt == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    if opt == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    if opt == 3:
        if n1 == n2:
            print('Os números {} são iguais'.format(n1))
        if n1 > n2:
            print('{} é o MAIOR.'.format(n1))
        if n2 > n1:
            print('{} é o MAIOR.'.format(n2))
    if opt == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
print('Fim do programa')
