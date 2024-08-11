# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print(f"""Letra A aparece {frase.count("A")} vezes
Primeira posição em {frase.find("A")+1}
Última posição em {frase.rfind("A")+1}""")
