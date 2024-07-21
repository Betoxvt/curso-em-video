# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo sera negado.
vc = float(input('Qual o valor da casa? R$'))
sc = float(input('Qual o salário do comprador? R$'))
a = float(input('Quantos anos para pagar? '))
p = vc / (a * 12)
print(f'Valor da prestação mensal: \033[1:34mR${p:.2f}\033[m')
if p > sc * 0.3:
    print('\033[1:31mEmpréstimo negado.\033[m')
else:
    print('\033[1:32mEmpréstimo aprovado.\033[m')
