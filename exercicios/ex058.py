# Jogo da adivinhação v2.0
# Melhore o jogo do ex028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
continuar = 'S'
while continuar == 'S':
    print()
    print('\033[34m-=-\033[m'*19)
    print(f'\033[33m{'JOGO DA ADIVINHAÇÃO':^58}\033[m')
    print('\033[34m-=-\033[m'*19)
    print()
    # acertou = False
    # palpites = 0
    palpites = 1
    computador = randint(0, 10)
    jogador = int(input('Tente adivinhar em que número de 0 a 10 estou pensando! '))
    # while not acertou:
    while jogador != computador:
        # jogador = int(input('Qual é o seu palpite? '))
        palpites += 1
        # if jogador == computador:
            # acertou = True
        # else:
        if jogador < computador:
            jogador = int(input('Mais... Tente outra vez: '))
        else:  # elif jogador > computador:
            jogador = int(input('Menos... Tente outra vez: '))
    print()
    print('\033[34m-=-\033[m'*19)
    print('Você acertou na \033[1;33m{}ª\033[m tentativa! PARABÉNS!.'.format(palpites).center(58))  # ; pelo vscode
    print('\033[34m-=-\033[m'*19)
    print()
    continuar = str(input('Gostaria de jogar outra vez, [S/N]? ')).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Não entendi, sim ou não [S/N]? ')).upper().strip()[0]
print()
print('Foi divertido jogar com você! Até a próxima!')
print()
