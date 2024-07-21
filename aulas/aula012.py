# Condições Aninhadas
# if, elif, else

nome = str(input('Qual o seu nome? '))
if nome == 'Roberto':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Ângela Cláudia Jéssica Amélia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem comum...')
print('Tenha um bom dia, {}!'.format(nome))
