# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Preço: '))
np = p - (p * 0.05)
print(f'O preço do produto que custa {p}, com desconto de 5% ficou {np:.2f}')
