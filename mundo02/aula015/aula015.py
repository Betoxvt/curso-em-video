# INTERROMPENDO REPETIÇÕES
"""
while True
    if chão
        passo
    if buraco
        pula
    if moeda
        pega
    if troféu
        pula
        break
pega
"""
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')  # python 3.6+
print('A soma vale {}'.format(s))  # python 3
print('A soma vale %d' % s)  # python 2
