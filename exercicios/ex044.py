# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

p = float(input('Digite o preço do produto: '))
f = str(input('E sua forma de pagamento:'
              '\nCheque (1), Dinheiro (2) ou Cartão (3)? ')).lower().strip()
# Poderia usar opções numeradas também como no ex037, mas queria testar umas coisas;
if f in 'dinheiro cheque 1 2':
    print(f'10% de desconto, 1x R${p - (p * 0.1):.2f}')
else:
    x = int(input('Número de parcelas do pagamento: '))
pj = (p + (p * 0.2))

if f in 'dinheiro cheque 1 2':
    pass
elif f in 'cartão cartao 3' and x == 1:
    print(f'5% de desconto, 1x R${p - (p * 0.05):.2f}')
elif f in 'cartão cartao 3' and x == 2:
    print(f'2x R${p / 2:.2f} = R${p:.2f}')
elif f in 'cartão cartao 3' and x >= 3:
    print(f'{x}X R${pj / x:.2f} = R${pj:.2f}')
else:
    print('Por favor, confira a forma de pagamento e número de parcelas.')
print('Boas vendas!')
print('-' * 50)
