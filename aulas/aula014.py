# Estrutura de Repetição while
# Para quando não se sabe o limite de repetições por exemplo
# Estrutura de repetição com teste lógico
'''
while not maçã:
    passo
pega

while not maçã
    if chão
        passo
    if buraco
        pula
    if moeda
        pega
pega
'''

'''
for c in range(1, 10):
    print(c)
print('Fim')
'''
'''
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
'''
# Vai pedir 4 valores
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')

# Vai pedir valores enquanto o usuário definir que sim
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:  # Digitar 0 encerra o while
    n = int(input('Digite um valor: '))
    if n != 0:  # Para não considerar o 0 como número
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} num pares e {} num ímpares!'.format(par, impar))
