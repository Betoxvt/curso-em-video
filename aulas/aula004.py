# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
# de acordo com o valor digitado.
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))

# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre
# uma mensagem com a data formatada.
dia = input('Em que dia vc nasceu? ')
mes = input('De que mês? ')
ano = input('E em qual ano? ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')

# Crie um script Python que leia dois números e tente mostrar a soma entre eles.
print('*Calcular a soma entre dois números inteiros*')
n1 = input('Digite um número: ')
n2 = input('Agora o outro número: ')
print('A soma dos dois números é', n1 + n2, '!')
"""assim não faz a soma, faz a concatenação"""
