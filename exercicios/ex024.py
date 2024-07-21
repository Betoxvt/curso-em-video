# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Em que cidade você nasceu? ')).strip()  # Corrige se tiver espaços antes
print(cidade[:5].upper() == 'SANTO')  # Verifica se 'SANTO' ocupar os 5 primeiros caracteres
