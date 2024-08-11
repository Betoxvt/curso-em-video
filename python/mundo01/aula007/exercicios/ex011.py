# Pintando parede
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
area = l * h
t = area/2
print(f'Para uma parede {l} m X {h} m com {area} m² são necessários {t} l de tinta.')
