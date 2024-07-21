# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
print('Conversor de números para binário, octal ou hexadecimal')
n = int(input('Insira o número inteiro que deseja converter: '))
b = int(input('Para a base digite o seguinte:'
              '\n\033[1m[1]\033[m para \033[4mbinário\033[m'
              '\n\033[1m[2]\033[m para \033[4moctal\033[m'
              '\n\033[1m[3]\033[m para \033[4mhexadecimal\033[m'
              '\n\033[1mQual deseja?\033[m '))
if b == 1:
    print(f'\033[34mEm binário, o número "{n}" fica {bin(n)[2:]}\033[m')
elif b == 2:
    print(f'\033[34mEm octal, o número "{n}" fica {oct(n)[2:]}\033[m')
elif b == 3:
    print(f'\033[34mEm hexadecimal, o número "{n}" fica {hex(n)[2:]}\033[m')
else:
    print('\033[31mPor favor digite uma base válida.\033[m')
