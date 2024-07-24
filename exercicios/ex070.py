# Estatísticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
total = mdm = menor = c = 0
barato = ' '
while True:
    print('='*42)
    print('Registro de compra'.center(42))
    print('='*42)
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    total += preço
    c += 1
    if preço > 1000:
        mdm += 1
    if c == 1 or preço < menor:
        barato = nome
        menor = preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
totalf = str(f'R$ {total:.2f}').replace('.', ',')
baratof = str(f'{barato} de R$ {menor:.2f}').replace('.', ',')
print('Fim da compra')
print('='*42)
print(f'Total da compra:{totalf:>26}')
print(f'Produtos por mais de R$ 1000,00: {mdm:>9}')
print(f'Produto mais barato:{baratof:>22}')
print('='*42)
