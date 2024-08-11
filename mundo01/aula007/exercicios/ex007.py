# Média aritmética
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
a = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A média entre as notas {n1:.1f} e {n2:.1f} de {a} é {m:.1f}')
