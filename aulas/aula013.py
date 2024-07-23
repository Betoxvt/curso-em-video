# Estrutura de repetição (Laços, Iteração) "for" com variável de controle
# Parte 1

# Ex.1: for c in range(1,10):
#           passo
#       pega

# Ex.2:  for c in range(0,3):
#           passo
#           pula
#        passo
#        pega

# Ex.3:  for c in range(0,3):
#           if coin:                #Com estrutura de condição
#               pega
#           passo
#           pula
#        passo
#        pega

for c in range(1, 6):
    print('Oi')
print('Fim')

for c in range(1, 6):
    print(c)
print('Fim')

for c in range(6, 0, -1):
    print('Io')
print('Fim')

for c in range(0, 7):
    print(c)
print('Fim')

for c in range(0, 7, 2):
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n  # s = s + n
print(f'O somatório de todos os valores foi {s}')
