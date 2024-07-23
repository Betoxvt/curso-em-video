# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# Extra - Se for mulher está dispensada, se for homem tem que analisar
from datetime import date
sexo = str(input('Informe o sexo: ')).strip().upper()[0]
if sexo == 'F':
    print('Está dispensada do alistamento.')
else:
    nascimento = int(input('Digite o ano de nascimento: '))
    ano = date.today().year
    idade = ano - nascimento
    print(f'Jovem do sexo masculino com {idade} anos.')
    if idade < 18:
        print(f'O jovem ainda vai se alistar, daqui a {18 - idade} anos.')
    elif idade == 18:
        print('É hora do jovem se alistar')
    elif idade > 18:
        print(f'Já passou do tempo do alistamento há {idade - 18} anos.')
