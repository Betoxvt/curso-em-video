# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    pesos += [peso]
pord = sorted(pesos)
print(f'O maior peso é {pord[len(pord)-1]}Kg')
print(f'E o menor peso é {pord[0]}Kg.')

# Método da aula
# maior = 0
# menor = 0
# for p in range(1,6):
#     peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print...