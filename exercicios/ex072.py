# Número por extenso
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número inteiro entre 0 e 20: '))
        if 0 <= num <= 20:
            break
    print(f'O número digitado por extenso é {extensos[num]}')
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
print('Programa terminado')
