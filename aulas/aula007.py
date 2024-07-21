# Operadores Aritméticos
# + adição, - subtração, * multiplicação, / divisão, // divisão inteira, ** potência, % resto da divisão
soma = 5 + 2
subt = 5 - 2
mult = 5 * 2
pot = 5 ** 2  # pow(5,2) da também
divi = 5 / 2
dint = 5 // 2
rest = 5 % 2
print(soma, subt, mult, pot, divi, dint, rest)
# Ordem de precedência
# 1 ()
# 2 **
# 3 * / // %
# 4 + -
# Caso sejam de mesma ordem, calcula por ordem escrita
# n**(1/2) da raiz quadrada, n**(1/3) da raiz cúbica

# formatando str
nome = str(input('Qual o seu nome? '))
print('Prazer em te conhecer {}!'.format(nome))  # Normal
print('Prazer em te conhecer {:20}!'.format(nome))  # Em 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome))  # Em 20 caracteres e alinhado à direita
print('Prazer em te conhecer {:<20}!'.format(nome))  # Em 20 caracteres e alinhado à esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))  # Em 20 caracteres e centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome))  # Em 20 caracteres e centralizado e com '=' em volta

# Arredondando valores e formatando quebra de linha
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
e = n1 ** n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
print(f'A soma é {s}, o produto é {m}, a divisão é {d:.2f}', end=', ')  # end='' não quebra a linha
# :.2f entre as chaves, após a variável faz com que mostre apenas 2 dígitos após o ponto e arredonde
print(f'a divisão inteira é {di}, \n o resto é {r} \n e a potência é {e}')  # \n quebra a linha
