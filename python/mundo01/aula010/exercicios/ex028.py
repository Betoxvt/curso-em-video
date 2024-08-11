# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""from random import randint
n = randint(0, 5)
nu = int(input('Adivinhe o número que estou pensando, de 0 a 5: '))
if nu == n:
    print('Acertou miserávi!')
else:
    print('Errou! kkkk')
print(f'Pensei no número {n}')"""
from random import randint
computador = randint(0, 5)
print('\033[1:33:40m-=-\033[m' * 20)
print(f'{'\033[1:35:40m'}{'Vou pensar em um número entre 0 e 5. Tente adivinhar...':^60}{'\033[m'}')
print('\033[1:33:40m-=-\033[m' * 20)
jogador = int(input(f'{'\033[1:97:40m'}{'Em que número eu pensei? ':<60}{'\033[m'}'))
if jogador == computador:
    print('\033[1:32:40m-=-\033[m' * 20)
    print(f'{'\033[1:32:40m'}{'PARABÉNS! Você conseguiu me vencer!':^60}{'\033[m'}')
    print('\033[1:32:40m-=-\033[m' * 20)
else:
    print('\033[1:31:40m-=-\033[m' * 20)
    print(f'{'\033[1:31:40m'}{f'GANHEI! Eu pensei no número {computador} e não no {jogador}':^60}{'\033[m'}')
    print('\033[1:31:40m-=-\033[m' * 20)
