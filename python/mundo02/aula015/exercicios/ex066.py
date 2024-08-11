# Vários números com flag
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = c = s = 0
print('Digite os valores:'
      '\n[999] para parar')
while True:
    n = int(input('>>>> '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} números e a soma entre eles é {s}.')
