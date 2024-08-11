# Cores no Terminal

# Padrão ANSI escape sequence "\código
# \033[style;text;backmCOR]
# Ex.: \033[0;33;44m]

# Style melhores pro python
# 0 None Nenhum
# 1 Bold Negrito
# 4 Underline Sublinhado
# 7 Negative Inverso

# Text                     Back
# 30    Black   Preto      40
# 31    Red     Vermelho   41
# 32    Green   Verde      42
# 33    Yellow  Amarelo    43
# 34    Blue    Azul       44
# 35    Magenta (roxo)     45
# 36    Cyan    Ciano      46
# 37    Grey    Cinza      47
# 97    White   Branco     107

print('\033[7:33:44mOlá, Mundo!\033[m')
print('')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('')

nome = 'Roberto'
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1:30:107m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[30:107m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
