# Utilizando Módulos
# Nas primeiras linhas do programa se importa as bibliotecas/módulos
# import módulo (importa todas as funções do módulo)
# ex.: import math
# from módulo import função (importa só a função)
# ex.: from math import sqrt, ceil (sqrt e ceil)
# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print(f'A raiz de {num} é igual a {raiz}')
# print(f'A raiz de {num} é igual a {raiz:.2f}')
# print(f'A raiz de {num} é igual a {math.ceil(raiz)}')
# print(f'A raiz de {num} é igual a {math.floor(raiz)}')
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.2f}')
print(f'A raiz de {num} é igual a {floor(raiz)}')

import random
num = random.random()
num1 = random.randint(1, 10)
print(num, num1)

import emoji
print(emoji.emojize('Olá, mundo :earth_americas:', language='alias'))