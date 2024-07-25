# Maior e menor valores em tupla
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
n0 = randint(0, 9)
n1 = randint(0, 9)
n2 = randint(0, 9)
n3 = randint(0, 9)
n4 = randint(0, 9)
tup = (n0, n1, n2, n3, n4)
print(tup)
print(f'The greater number is {sorted(tup)[-1]}.')
print(f'And the lesser number is {sorted(tup)[0]}.')
