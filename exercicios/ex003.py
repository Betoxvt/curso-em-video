# Somando dois números
# Crie um script que leia 2 números e mostre a soma entre eles.
cor = {'limpa': '\033[m',
          'preto': '\033[30:107m',
          'branco': '\033[97:40m',
          'verde': '\033[32m'}

n1 = int(input(f'{cor['verde']}Digite um número: '))
n2 = int(input(f'{cor['verde']}Digite outro: {cor['limpa']}'))
s = n1 + n2
print(f'A soma entre {cor['branco']}{n1}{cor['limpa']} e {cor['preto']}{n2}{cor['limpa']} vale {cor['verde']}{s}{cor['limpa']}!')
