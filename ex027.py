# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente
# E.: Ana Maria de Souza
# primeiro = Ana
# último = Souza

n = str(input('Nome completo: ')).strip().title()
nome = n.split()
print(f'Primeiro nome: {nome[0]}')
print(f'Sobrenome: {nome[-1]}')  # ou {nome[len(nome)-1]}
