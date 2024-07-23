# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Salário: '))
ns = s + (s * 0.15)
print(f'Para um funcionário com salário de {s}, o novo salário com 15% de aumento é {ns:.2f}')
