# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores digitados.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = media = maior = menor = num = int(input('Digite um nº inteiro: '))
c = 1
continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
while continuar not in 'SN':
    continuar = str(input('Digite apenas "S" ou "N"')).strip().upper()[0]
while continuar == 'S':
    num = int(input('Digite um nº inteiro: '))
    c += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite apenas "S" ou "N"')).strip().upper()[0]
print('-=-' * 10)
print(f'Analisando os {c} números:')
print(f'Média = {soma / c:.2f}')
print(f'Maior = {maior}')
print(f'Menor = {menor}')
print('-=-' * 10)
'''
# Método da aula
resp = 'S'
soma = quant = média = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
'''