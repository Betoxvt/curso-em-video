# Players record
# Do a program with the function record(), it receives two optional parameters: players name and how many goals he scored. The program must be able to show the players record, even if some data is missing or incorrect.
def record(name='', goals=''):
    if name.strip() == '':
        name = "<unknown>"
    if goals.isnumeric() == False:
        goals = "0"
    print(f"Player {name} scored {goals} goal(s) in the tournament.")
    
 
# Main program
record(str(input("Player's name: ")), str(input("Player's score: ")))

# Teacher Guanabara solution - uses integer, best to analyze number of goals

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')



# Programa principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

