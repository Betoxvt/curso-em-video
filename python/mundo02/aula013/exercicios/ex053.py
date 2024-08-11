# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços e acentos.
# Ex.: APOS A SOPA
# Ex.: A SACADA DA CASA
# Ex.: A TORRE DA DERROTA
# Ex.: O LOBO AMA O BOLO
# Ex.: ANOTARAM A DATA DA MARATONA

frr = str()
fraze = (str(input('Digite uma frase: ')))
print('')
frase = (fraze.upper().strip().replace('Á', 'A')
         .replace('É', 'E').replace('Í', 'I').replace('Ó', 'O')
         .replace('Ú', 'U').replace('À', 'A').replace('Ã', 'A')
         .replace('Õ', 'O').replace('Â', 'A').replace('Ê', 'E')
         .replace('Ô', 'O'))
fr = (frase.replace(' ', '').replace('.', '').replace('!', '')
      .replace('-', '').replace('_', '').replace('?', ''))

print('Para verificar se a frase é um palíndromo, não vamos considerar os acentos, ficando assim:')
print(frase)
print('')
print('Agora removemos os espaços, deixando somente as letras na ordem digitada...')
print(f'\033[32m{fr}\033[m')
print('')

for c in range(len(fr)-1, -1, -1):
    frr += fr[c]

print('Veja agora como ficou lendo de trás para a frente:')
print(f'\033[31m{frr}\033[m')
print('')

if frr == fr:
    print('Esta frase \033[4mÉ\033[m um palíndromo!')
else:
    print('Esta frase \033[4mNÃO É\033[m um palíndromo!')

# Também podemos fazer sem o for

inverso = fr[::-1]
print(inverso)