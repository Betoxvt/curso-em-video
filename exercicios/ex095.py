# Enhancing Dictionaries
# Enhance the ex093 to work with multiple players, including a player goal-score record detail visualization system.
team = list()
while True:
    player = {'Name': input('Name: ').strip().title(),
              'Matches': int(input('Matches: ')),
              'Goals': list()}
    for m in range(1, player['Matches'] + 1):
        player['Goals'].append(int(input(f'Match number {m}, goals score: ')))
    player['Total'] = (sum(player['Goals']))
    team.append(player.copy())
    while True:
        ans = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()[0]
        if ans in 'YN':
            break
        print('Please enter "Y" or "N".')
    if ans == 'N':
        break
print('—' * 68)
print(f'Id{' ':4}', end='')
for i in player.keys():
    print(f'{i:<18}', end='')
print()
print('-' * 68)
for k, v in enumerate(team):
    print(f'{k:>2}{' ':4}', end='')
    for d in v.values():
        print(f'{str(d):<18}', end='')
    print()
print('—' * 68)
while True:
    Id = int(input('Which player [Id] are you interested in? (999 to exit) '))
    if Id == 999:
        break
    if Id >= len(team) or Id < 0:
        print('Please enter a valid player Id.')
    else:
        print(f'> Details from player {team[Id]["Name"]} <'.center(48, '='))
        for g in range(0, len(team[Id]['Goals'])):
            print(f'Match {g + 1}: {team[Id]['Goals'][g]} goals'.center(48))
        print('—'*68)
print(' END OF PROGRAM '.center(48, '-'))
