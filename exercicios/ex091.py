# Dice game
# Create a program where 4 players throw a dice and get random results. Save the results in a dictionary.
# At the end, put this dictionary in order, knowing that the winner got the highest dice throw number.
from random import randint
from time import sleep
from operator import itemgetter  # Needed in teacher's solution
turn = []
input('Throw the dice! [ENTER]')
sleep(1)
for i in range(1, 5):
    throw = {'Player': i, 'throw': randint(1, 6)}
    turn.append(throw.copy())
turn.sort(key=lambda value: value['throw'], reverse=True)
print("And the results are...")
sleep(1)
for i, v in enumerate(turn, start=1):
    print(f"{i}º place: Player", v['Player'], "with", v['throw'])
    sleep(1)
print(f'Congratulations! Player {turn[0]["Player"]} wins!')

# Later, in case of a tie, a tie-breaking procedure will be implemented.

# Teacher's Solution
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} tirou {v[1]}.')
    sleep(1)
