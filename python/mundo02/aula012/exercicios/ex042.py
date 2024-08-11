# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
print('\033[4mSerá possível formar um triângulo? Insira o valor das arestas:\033[m')
a1 = float(input('Primeiro valor: '))
a2 = float(input('Segundo valor: '))
a3 = float(input('Terceiro valor: '))
if a1 < a2 + a3 and a2 < a1 + a3 and a3< a1 +a2:
    print('\033[1:32mÉ possível formar um triângulo\033[m')
    if a1 == a2 == a3:
        print('\033[1:34mEQUILATERO\033[m')
    elif a1 != a2 != a3 != a1:  # atenção na forma que lê! a1 != a2 / a2 != de a3 / a3 != de a1
        print('\033[1:34mESCALENO\033[m')
    else:
        print('\033[1:34mISSOSCELES\033[m')
else:
    print('\033[1:31mNão é possível formar um triângulo\033[m')
