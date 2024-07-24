# Tabuada v3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('Programa Tabuada v3.0 Iniciado')
while True:
    print('-' * 38)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 38)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:>2} = {n * c}')
print('Programa Tabuada encerrado')
