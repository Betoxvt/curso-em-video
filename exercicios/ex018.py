# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
a = float(input('Digite o ângulo (em graus): '))
ar = radians(a)
print(f'O ângulo de {a}º tem:\nSENO {sin(ar):.2f}\nCOSSENO {cos(ar):.2f}\nTANGENTE {tan(ar):.2f}')
