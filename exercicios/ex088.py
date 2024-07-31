# Mega-Sena (lottery) tickets generator
# Create a program that generates random Mega-Sena number sets.
# The program will ask the user for the desired amount tickets and then generate six random numbers
# between 1 and 60 for each ticket, storing them in a nested list.
from random import randint
from time import sleep
tickets = []
ticket = []
print('—'*36)
print(f'{'Mega-sena ticket generator':^36}')
print('—'*36)
amount = int(input('How many tickets? '))
print(f'  Generating {amount} tickets...  '.center(36, '='))
for t in range(0, amount):
    n = 0
    while n < 6:
        num = (randint(1, 60))
        if num not in ticket:
            ticket.append(num)
            n += 1
    ticket.sort()
    tickets.append(ticket[:])
    ticket.clear()
sleep(1)
for ts, t in enumerate(tickets):
    print(f'Ticket {ts+1}: {t}')
    sleep(0.7)
print('  Good luck!  '.center(36, '='))

# Teacher's solution
# from random import randint
# from time import sleep
# lista = list()
# jogos = list()
# print('-' * 30)
# print('      JOGA NA MEGA SENA      ')
# print('-' * 30)
# quant = int(input('Quantos jogos você quer que eu sorteie? '))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#             if cont == 6:
#                 break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')
#     sleep(1)
# print('-=' * 5, f'< BOA SORTE >', '-=' * 5)
