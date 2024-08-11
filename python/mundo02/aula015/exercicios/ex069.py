# Análise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
maiores = homens = mulheres = 0
while True:
    print('='*42)
    print('CADASTRE UMA PESSOA'.center(42))
    print('='*42)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Fim do programa.')
print('='*42)
print(f'Total de pessoas com mais de 18 anos:   {maiores}')
print(f'Total de homens cadastrados:            {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}')
print('='*42)
