# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('\033[1:31m*-' * 20 + '*\033[m')
print(f'{'\033[1:34mHora de jogar JoKenPô!!!\033[m':^49}')
print('\033[1:31m*-' * 20 + '*\033[m')

computador = randint(1, 3)
jogador = int(input(' \033[1:37mPEDRA [1]\033[m, \033[1:97mPAPEL [2]\033[m ou \033[1:35mTESOURA [3]\033[m?: '))
print('\033[1:31m*-' * 20 + '*\033[m')
# fazer algo para transformar em str com as cores???
sleep(0.5)
print('\033[1:37mJo!')
sleep(1)
print('\033[1:97mKen!')
sleep(1)
print('\033[1:35mPô!')
sleep(1)

# Guanabara fez um bem mais simples -_-

print('\033[1:31m*-' * 20 + '*\033[m')
if computador == 1 and jogador == 1:
    print('Computador: \033[1:37mPEDRA\033[m'
          '\nJogador: \033[1:37mPEDRA\033[m')
    print('\033[1:31m*-' * 20 + '*\033[m')
    print('\033[1:36m-=-\033[m' * 5, '\033[1:34mEmpate...\033[m', '\033[1:36m-=-\033[m' * 5)
elif computador == 1 and jogador == 2:
    print('Computador: \033[1:37mPEDRA\033[m'
          '\nJogador: \033[1:97mPAPEL\033[m')
    print('\033[1:36m-=-\033[m' * 2, '\033[1:34mParabéns!!! Você me venceu!\033[m', '\033[1:36m-=-\033[m' * 2)
elif computador == 1 and jogador == 3:
    print('Computador: \033[1:37mPEDRA\033[m'
          '\nJogador: \033[1:35mTESOURA\033[m')
    print('\033[1:31m*-' * 20 + '*\033[m')
    print('\033[1:36m-=-\033[m' * 4, '\033[1:34mEssa eu venci!!\033[m', '\033[1:36m-=-\033[m' * 4)
elif computador == 2 and jogador == 2:
    print('Computador: \033[1:97mPAPEL\033[m'
          '\nJogador: \033[1:97mPAPEL\033[m')
    print('\033[1:31m*-' * 20 + '*\033[m')
    print('\033[1:36m-=-\033[m' * 5, '\033[1:34mEmpate...!\033[m', '\033[1:36m-=-\033[m' * 5)
elif computador == 2 and jogador == 1:
    print('Computador: \033[97mPAPEL\033[m'
          '\nJogador: \033[1:37mPEDRA\033[m')
    print('\033[1:31m*-' * 20 + '*\033[m')
    print('\033[1:36m-=-\033[m' * 4, '\033[1:34mEssa eu venci!!\033[m', '\033[1:36m-=-\033[m' * 4)
elif computador == 2 and jogador == 3:
    print('Computador: \033[97mPAPEL\033[m'
          '\nJogador: \033[1:35mTESOURA\033[m')
    print('\033[1:31m*-' * 20 + '*\033[m')
    print('\033[1:36m-=-\033[m' * 2, '\033[1:34mParabéns!!! Você me venceu!\033[m', '\033[1:36m-=-\033[m' * 2)
elif computador == 3 and jogador == 3:
    print('Computador: \033[1:35mTESOURA\033[m'
          '\nJogador: \033[1:35mTESOURA\033[m')
    print('\033[1:31m*-' * 20 + '*\033[m')
    print('\033[1:36m-=-\033[m' * 5, '\033[1:34mEmpate...\033[m', '\033[1:36m-=-\033[m' * 5)
elif computador == 3 and jogador == 1:
    print('Computador: \033[1:35mTESOURA\033[m'
          '\nJogador: \033[1:37mPEDRA\033[m')
    print('\033[1:31m*-' * 20 + '*\033[m')
    print('\033[1:36m-=-\033[m' * 2, '\033[1:34mParabéns!!! Você me venceu!\033[m', '\033[1:36m-=-\033[m' * 2)
elif computador == 3 and jogador == 2:
    print('Computador: \033[1:35mTESOURA\033[m'
          '\nJogador: \033[1:97mPAPEL\033[m')
    print('\033[1:31m*-' * 20 + '*\033[m')
    print('\033[1:36m-=-\033[m' * 4, '\033[1:34mEssa eu venci!!\033[m', '\033[1:36m-=-\033[m' * 4)
else:
    print(f'\033[1:30:41m{'Essa opção não existe no JoKenPô!':^41}\033[m')
print('\033[1:31m*-' * 20 + '*\033[m')
