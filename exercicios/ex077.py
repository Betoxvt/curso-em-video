# Contando vogais em tupla
# Crie um programa que tenha uma tupla com várias palavras (não use acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tup = ('journey', 'python', 'screen', 'code', 'computer', 'vowels', 'exercises', 'show')
vowels = ''
for i in tup:
    print(f'\nThe word "{i}" has the vowels:', end=' ')
    for j in i:
        if j in 'aeiou':
            vowels += f'"{j}", '
    vowels = vowels[:-2]
    print(vowels[::-1].replace(',', ' and'[::-1], 1)[::-1])
    vowels = ''
