# Compound variables – Dictionary
# Items == { Keys : Values }

####################################################################################################

# filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
# print(filme.values())  # dict_values(['Star Wars', 1977, 'George Lucas'])
# print(filme.keys())  # dict_keys(['titulo', 'ano', 'diretor'])
# print(filme.items())  # dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')]) tuples
#
# for k, v in filme.items():
#     print(f'O {k} é {v}')
#     # O titulo é Star Wars
#     # O ano é 1977
#     # O diretor é George Lucas

##################################################################################################

# locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
#             {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
#             {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]
#
# print(locadora[0]['ano'])  # 1977
# print(locadora[2]['titulo'])  # Matrix

#####################################################################################################################

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas)  # {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# # print(pessoas[0])  # error
# print(pessoas['nome'])  # Gustavo
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')  # O Gustavo tem 22 anos (Watch out for the quotation marks)
#
# for k in pessoas.keys():
#     print(k)  # nome / sexo /idade (each in new lines)
# for k, v in pessoas.items():
#     print(f'{k} = {v}')  # nome = Gustavo / sexo = M / idade = 22
#
# del pessoas['sexo']  # deletes element sexo (value and key).
# pessoas['nome'] = 'Leandro'  # Set the 'name' key to 'Leandro'.
# pessoas['peso'] = 98.5  # Set the 'weight' key in the dictionary to 98.5.
# print(pessoas)  # {'nome': 'Leandro', 'idade': 22, 'peso': 98.5}

#############################################################################################################

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
#
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(estado1)  # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# print(estado2)  # {'uf': 'Sao Paulo', 'sigla': 'SP'}
# print(brasil)  # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'Sao Paulo', 'sigla': 'SP'}]
# print(brasil[0])  # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# print(brasil[1])  # {'uf': 'Sao Paulo', 'sigla': 'SP'}
# print(brasil[0]['uf'])  # Rio de Janeiro

##################################################################################################################

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # Watch out, use .copy() to avoid aliasing between variables
print(brasil)  # [{'uf': 'BAHIA', 'sigla': 'BA'}, {'uf': 'PARANA', 'sigla': 'PR'}, {'uf': 'PARA', 'sigla': 'PA'}]
for e in brasil:  # {'uf': 'BAHIA', 'sigla': 'BA'} ...
    print(e)
for e in brasil:
    for k, v in e.items():      # uf: BAHIA...
        print(f'{k}: {v}')      # sigla: BA...
for e in brasil:
    for v in e.values():        # BAHIA BA...
        print(v, end=' ')
    print()
