# Jogo do par ou ímpar
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só sera interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
from random import randint
from time import sleep
print('-' * 30)
print('Vamos jogar Par ou Ímpar'.center(30))
print('-' * 30)
vc = 0
while True:
    r = 0
    nc = randint(0, 10)
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    nj = int(input('Digite um valor: '))
    print('-=-' * 10)
    sleep(1)
    print(f'Você jogou {nj} e eu {nc}.')
    print('-=-' * 10)
    s = nc + nj
    r = s % 2
    sleep(1)
    print(f'Deu {s}...')
    sleep(0.6)
    print(f'É PAR!' if r % 2 == 0 else 'É ÍMPAR!')
    if r == 0:
        sleep(0.6)
        if pi == 'P':
            vc += 1
            print('Você VENCEU!')
            print('-' * 30)
            print('Vamos jogar novamente!')
        else:
            print('Você PERDEU!')
            break
    elif r != 0:
        sleep(0.6)
        if pi in 'IÍ':
            vc += 1
            print('Você VENCEU!')
            print('-' * 30)
            print('Vamos jogar novamente!')
        else:
            print('Você PERDEU!')
            break
print('-' * 30)
sleep(0.6)
print('GAME OVER')
print('-' * 30)
print(f'Total de vitórias consecutivas: {vc}')
