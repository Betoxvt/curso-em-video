# Dice game
# Create a program where 4 players throw a dice and get random results. Save the results in a dictionary.
# At the end, put this dictionary in order, knowing that the winner got the highest dice throw number.
from random import randint
from time import sleep
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
