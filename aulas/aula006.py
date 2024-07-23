# Crie um script Python que leia dois números e tente mostrar a soma entre eles.
print('*Calcular a soma entre dois números inteiros*')
n1 = int(input('Digite um número: '))
n2 = int(input('Agora o outro número: '))
s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'é', s) ultrapassado
# print('A soma entre {} e {} vale {}'.format(n1, n2, s)) já ficou antigo
print(f'A soma entre {n1} e {n2} vale {s}')

n = input('Digite um valor: ')
# print('É numérico?', n.isnumeric())
# print('É alfabético?', n.isalpha())
# print('É alfanumérico?', n.isalnum())
# print('Somente letras maiúsculas?', n.isupper())
# Enfim... vários típos
print(type(n))