# Dissecando uma variável
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele
r = {'r': '\033[1:97m', 'l': '\033[m'}
n = input(f'{r['r']}Digite algo: ')
print('É numérico?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Somente letras maiúsculas?', n.isupper())
print('Somente letras minúsculas?', n.islower())
print('É ASCII?', n.isascii())
print('É imprimível?', n.isprintable())
print('Todas as palavras começam com letra maiúscula?', n.istitle())
print('Somente espaços em branco?', n.isspace())
print('É um identificador válido?', n.isidentifier())
print('Todos os caracteres são dígitos?', n.isdigit())
print('Todos os caracteres são decimais?', n.isdecimal())
print('O tipo primitivo desse valor é ', type(n))
