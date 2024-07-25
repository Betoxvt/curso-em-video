# Tuplas com teams de futebol
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) os últimos 4 colocados da tabela.
# C) Uma lista com os teams em ordem alfabética.
# D) Em que posição na tabela está o time de Criciúma.
teams = ('Botafogo', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Cruzeiro',
         'São Paulo', 'Bahia', 'Paranaense', 'Bragantino', 'Atlético Mineiro',
         'Vasco', 'Juventude', 'Internacional', 'Criciúma', 'Corinthians',
         'Cuiaba', 'Vitoria', 'Grêmio', 'Fluminense', 'Goianiense')
print(f'A) Top 5: {teams[0:5]}')
print(f'B) Last 4: {teams[-4:]}')
print(f'C) Alphabetical order: {sorted(teams)}')
print(f'D) Criciúma position: {teams.index("Criciúma") + 1}')
