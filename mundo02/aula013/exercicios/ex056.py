# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

p1 = []
p2 = []
p3 = []
p4 = []

for c in range(1, 5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome: ').strip().title())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper()[0])

    if c == 1:
        p1 = [nome, idade, sexo]
    elif c == 2:
        p2 = [nome, idade, sexo]
    elif c == 3:
        p3 = [nome, idade, sexo]
    elif c == 4:
        p4 = [nome, idade, sexo]

todos = [p1, p2, p3, p4]

mig = (todos[0][1] + todos[1][1] + todos[2][1] + todos[3][1]) / len(todos)
print(f'A média de idade do grupo é {mig} anos.')

h = []
m = []

for c in range(0, len(todos)):
    if todos[c][2] == 'M':
        h += [todos[c]]
    else:
        m += [todos[c]]

if len(h) > 1:
    hs = sorted(h, key=lambda x: (x[1]), reverse=True)
    if hs[0][1] > hs[1][1]:
        print(f'O homem mais velho é {hs[0][0]}, ele tem {hs[0][1]} anos.')
    else:
        hii = [hs[0][0]]
        for c in range(0, len(hs)-1):
            if hs[c][1] != hs[c+1][1]:
                break
            else:
                hii += [hs[c + 1][0]]
        hii2 = ', '.join(hii)
        hii3 = hii2[::-1].replace(','[::-1], ' e'[::-1], 1)[::-1]
        print(f'Os homens mais velhos são {hii3}, eles têm {hs[0][1]} anos.')
elif len(h) == 1:
    print(f'Só há um homem, {h[0][0]}, ele tem {h[0][1]} anos.')
else:
    print('Não há homens na lista.')

mm = 0
if len(m) > 1:
    for c in range(0, len(m)):
        if m[c][1] < 20:
            mm += 1
    if mm > 1:
        print(f'{mm} mulheres têm menos de 20 anos.')
    else:
        print(f'{mm} mulher tem menos de 20 anos.')
elif len(m) == 1:
    if m[0][1] < 20:
        print(f'Só há uma mulher com menos de 20 anos, {m[0][0]}.')
    else:
        print('Não há mulheres com menos de 20 anos.')
else:
    print('Não há mulheres na lista.')
