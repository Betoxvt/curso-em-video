# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Que ano você quer saber se é BISSEXTO? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[1m{ano}\033[32m é\033[m bissexto!')
else:
    print(f'O ano \033[1m{ano}\033[31m não é\033[m bissexto!')
