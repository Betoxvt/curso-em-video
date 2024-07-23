# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
km = float(input('Quantos km foram rodados? '))
d = int(input('Quantos dias alugados? '))
pk = 0.15
pd = 60
ck = km * pk
cd = d * pd
ct = ck + cd
print(f'O valor total a pagar, ficou em R$ {ct:.2f}')
