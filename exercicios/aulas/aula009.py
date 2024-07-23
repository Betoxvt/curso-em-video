# Manipulando Texto (cadeia de caracteres ou string)
frase = 'Curso em Video Python'

# Fatiamento de string
print(frase)
print(frase[9])             # Exibe o caractere fatiado na posição 9 da string (começa por 0)
print(frase[9:13])          # Pega do 9 ao 12, o último valor não entra na contagem
print(frase[9:21])          # Fatia também (a string termina no 20, portanto exibe até o fim)
print(frase[9:21:2])        # Pulando de 2 em 2
print(frase[:5])            # Começa do início ao 4
print(frase[15:])           # Até o final
print(frase[9::3])

# Análise
print(len(frase))           # Exibe o comprimento da string em caracteres
print(frase.count('o'))     # Conta quantas vezes aparece a letra o (minúscula)
print(frase.count('o', 0, 13))
print(frase.find('deo'))    # Aponta em que posição começa a 'deo'
print(frase.find('Android'))  # -1 indica que não existe
print('curso' in frase)     # Existe curso na frase?
print(frase.lower().find('vídeo'))  # Coloca tudo em minúsculo e aí consegue procurar 'vídeo'

# Transformação
fr = frase.replace('Python', 'Android')  # Substitui
print(fr)
print(frase.upper())  # Tudo em maiúsculo
print(frase.lower())  # Tudo para minúsculo
print(frase.capitalize())  # Joga tudo para minúsculo e a primeira letra em maiúsculo
print(frase.title())  # Primeira letra de cada palavra fica maiúscula

f2 = '   Aprenda Python  '
print(f2)
print(f2.strip())   # Remove todos os espaços inúteis no início e no fim da frase (mantém entre as palavras)
print(f2.rstrip())  # Remove da direita
print(f2.lstrip())  # Remove da esquerda

# Divisão
fd = frase.split()  # Estudar: cria divisão nos espaços, recomeça os indices para cada str (gera uma lista)
print(fd)
print(fd[0])  # Mostra a 1ª da lista
print(fd[2][3])  # Mostra o 4º caractere da 3ª str da lista

# Junção
print('_'.join(fd))  # Junta as palavras da lista novamente, o que separa é '_', mas pode ser qualquer

# Prática com len()
frase = '  Curso em    Vídeo Python  '
print(frase)
print(len(frase))
print(frase.strip())
print(len(frase.strip()))
print(frase.split())
print(len(frase.split()))
print(' '.join(frase.split()))
print(len(' '.join(frase.split())))
print(''.join(frase.split()))
print(len(''.join(frase.split())))  # Conta o comprimento sem espaços
