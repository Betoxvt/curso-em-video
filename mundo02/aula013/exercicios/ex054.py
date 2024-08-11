# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = int(0)
menor = int(0)

# Para saber a posição use lista [] e a quantidade use len()

for c in range(1, 8):
    ano = int(input(f'Digite o ano da {c}ª pessoa: '))
    if atual - ano >= 18:
        maior += (c - (c-1))
    else:
        menor += (c - (c-1))
print(f'{maior} pessoas maiores de 18 anos.')
print(f'{menor} pessoas menores de 18 anos.')
