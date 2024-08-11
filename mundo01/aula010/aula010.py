# Condições (Parte 1)
# Simples, Compostas e Simplificadas

tempo = int(input('Quantos anos tem seu carro? '))

# Composta
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')

# Mais simplificado, porém, pode ficar um pouco confuso
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--Fim--')

# Simples
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo!')
# Composta
else:
    print('Que nome comum...')
print('Bom dia, {}!'.format(nome))

# Composta
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')

# Simplificada
print('Aprovado' if m >= 6 else 'Reprovado')
