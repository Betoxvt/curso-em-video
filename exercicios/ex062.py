# Melhore o ex061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-=-' * 6)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
f = 0
m = 10
print('Os dez primeiros termos da P.A. são:')
while m != 0:
    f = f + m
    while c <= f:
        print(p, end=' → ')
        p += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos a mais: '))
print(f'P.A. com um total de {f} termos.')
print('Fim do programa')
