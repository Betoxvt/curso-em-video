# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.
print('Formará um triângulo? Insira o comprimento de três retas...')
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mÉ possível formar um triângulo!')
else:
    print('\033[31mNão é possível formar um triângulo!')
