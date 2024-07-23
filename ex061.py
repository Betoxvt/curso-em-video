# PROGRESSÃO ARITMÉTICA v2.0
# Refaça o ex051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
print('Os dez primeiros termos da P.A. são:')
while c != 9:
    print(f'{p}', end=' → ')
    p = p + r
    c += 1
print(f'{p + r}')
