# Melhore o ex061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
f = 10
m = 1
print('Os dez primeiros termos da P.A. são:')
while m != 0:
    while c < f:
        print(p, end=' → ')
        p += r
        c += 1
    print(p)
    print('Insira [0] para sair do programa\nOu')
    m = int(input('Quantos termos a mais: '))
    if m > 0:
        print('Continuando a partir do último termo...')
        f += m
    elif m < 0:
        f -= m
        print('Vou considerar como positivo.')
        print('Continuando a partir do último termo...')
print('Fim do programa')
