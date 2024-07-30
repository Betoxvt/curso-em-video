# Compound variables - List (part2)
# Nested lists
# teste = list()
# teste.append('Gustavo')  # ['Gustavo']
# teste.append(40)  # ['Gustavo', 40]
# galera = list()
# galera.append(teste[:])  # Attention! Avoid aliasing between lists, using [:]
# teste[0] = 'Maria'  # ['Maria', 40]
# teste[1] = 22  # ['Maria', 22]
# galera.append(teste[:])  # ['Gustavo, 40] + ['Maria', 22]
# print(galera)  # prints [['Gustavo', 40], ['Maria', 22]]
#                 0             1               2               3
#              0      1      0     1        0       1       0      1
# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[2][1])  # prints 13
# for p in galera:
#     print(p)  # prints the list ['João', 19]...
#     print(p[0])  # only names
#     print(p[1])  # only ages
#     print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))  # dado == ['Nome']
    dado.append(int(input('Idade: ')))  # dado == ['Nome', Idade]
    galera.append(dado[:])  # galera == [[dado],[dado], ...] again, copy so you dont make an alias
    dado.clear()  # dado == []
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
