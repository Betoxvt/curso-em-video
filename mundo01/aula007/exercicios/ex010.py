# Conversor de moedas
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27
din = float(input('Quantos dinheiro você tem na carteira? R$ '))
dol = din / 3.27
print(f'Você pode comprar aproximadamente US$ {dol:.2f}.')
