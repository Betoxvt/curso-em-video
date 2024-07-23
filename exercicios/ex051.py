# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética (PA).
# No final, mostre os 10 primeiros termos dessa progressão.

i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
f = r * 10 + i
for c in range(i, f, r):
    if c < f-r:
        print(c, end=' → ')
    else:
        print(c)
print('FIM')
