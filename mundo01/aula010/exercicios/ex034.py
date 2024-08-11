# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual o salário do funcionário? R$ '))
if s > 1250:
    print(f'O valor do aumento é de R$ {s * 0.1} totalizando R$ {s * 1.1:.2f}')
else:
    print(f'O valor do aumento é de R$ {s * 0.15} totalizando R$ {s * 1.15:.2f}')
