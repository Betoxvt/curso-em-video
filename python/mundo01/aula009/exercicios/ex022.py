# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(nome.upper())
print(nome.lower())
print(f'Seu nome tem ao todo: {len(''.join(nome.split()))} letras')
print(f'Seu primeiro nome tem: {len(nome.split()[0])} letras')

# ou
# print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
