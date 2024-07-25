# Lista de preços com tupla
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tup = ('Mouse', 66.99, 'Keyboard', 89.90, 'Monitor', 480, 'Case', 330, 'Laptop', 5399, 'WebCam', 180,
       'Mouse Pad', 12.50, 'Power Supply Unit', 205.6)
c = 0
print('-'*40)
print(f'{'Tabela de produtos':^40}')
print('='*40)
while c < len(tup)-1:
    valor = str(f'R$ {tup[c+1]:.2f}').replace('.', ',')  # Changed dot for comma just for practice,
    print(f'{tup[c]:.<20}{valor:.>20}')                               # to fit the brazilian standard.
    c += 2
