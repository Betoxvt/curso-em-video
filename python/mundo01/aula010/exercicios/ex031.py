# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
dist = int(input('Qual a distância da viagem em km? '))
if dist <= 200:
    print(f'O preço da passagem ficou: R$ {dist*0.5:.2f}')
else:
    print(f'O preço da passagem ficou: R$ {dist*0.45:.2f}')

# simplificada
# preço = dist * 0.50 if dist <= 200 else distância * 0.45
# print(f'O preço... {preço:.2f}')
