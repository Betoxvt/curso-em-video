# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(co, ca) # Sem o math fica (co ** 2 + ca ** 2) ** (1 / 2)
print(f'A hipotenusa deste triângulo retângulo mede {hip:.2f}')
