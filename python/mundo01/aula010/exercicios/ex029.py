# Escreve um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.
v = int(input('Velocidade do carro em km/h: '))
if v > 80:
    print(f'Velocidade acima do limite de 80 km/h, a multa é de R$ {(v - 80) * 7:.2f}')
print('Tenha um bom dia!')
