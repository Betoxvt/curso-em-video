# Faça um programa que mostre na tela uma contagem regressiva pro estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

input('Aperte ENTER para iniciar a contagem regressiva dos fogos')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('*')
