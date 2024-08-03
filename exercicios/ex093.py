# Soccer player registration
# Create a program that manages the goal-scoring record of a soccer player.
# The program reads the name and how many matches he/her played.
# After that, will read how many goals the player made on each match.
# At the end, all the data will be stored in a dictionary, including total of goals mande during the championship.
# The point is to practice the use of dictionary type variable, don't be lazy.
player = {'Name': input('Name: '),
          'Matches': int(input('Matches: ')),
          'Goals': list()}
for m in range(1, player['Matches'] + 1):
    player['Goals'].append(int(input(f'Match number {m}, goals score: ')))
player['Total'] = (sum(player['Goals']))
print('—'*68)
print(player)
print('—'*68)
for k, v in player.items():
    print(f'{k}: {v}')
print('—'*36)
print(f'Player {player["Name"]} acted in {player["Matches"]} matches.')
for m, g in enumerate(player["Goals"], start=1):
    print(f'    => Match {m}: {g} goals.')
print(f'Scored {player["Total"]} goals in the championship.')
