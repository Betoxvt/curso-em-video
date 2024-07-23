# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
print('Insira 3 número para saber qual é o menor e qual é o maior...')
a = int(input('N1: '))
b = int(input('N2: '))
c = int(input('N3: '))
lista = [a, b, c]
lista.sort()
print(lista[0], 'é o menor')
print(lista[2], 'é o maior')

# Maneira 2
# if a < b and a < c:
#    menor = a
# Aí faz para todas as letras, e o mesmo depois para o maior;

# Maneira 3
# menor = a
# if b < a and b < c:
#    menor = b
# if c < a and c < b:
#    menor = c
# Similar para o maior

# Maneira 4
# print('O maior número é ', max(lista))
# print('O menor número é ', min(lista))
