# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, conforme a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda e última nota: '))
m = (n1 + n2) / 2
print(f'Média final {m:.1f}')
if m < 5:
    print('REPROVADO')
elif m >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
