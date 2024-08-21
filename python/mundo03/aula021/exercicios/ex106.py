# Create a mini-system which uses Interactive Help from Python.
# User will type a command then the manual will be displayed.
# Program stops when user type "END".
# Observation: Use colors!

s = (                           # Styles
           '\033[m',            # No style [0]
           '\033[1;30;42m',     # Bold + Black letters + Green background   [1]
           '\033[1;30;43m',     # Bold + Black letters + Yellow backgroud   [2]
           '\033[1;30;45m',     # Bold + Black letters + Magenta background [3]
           '\033[1;97;47m',     # Bold + White letters + Grey background    [4]
           '\033[1;30;107m'     # Bold + Black letters + White background   [5]
           )

def special_help(cmd):
    from time import sleep
    header(f'Printing {cmd} manual', 2)
    sleep(1)
    print(s[5])
    print(eval(cmd).__doc__, end='')
    print(s[0], end='')
    sleep(2)


def header(msg, style=0):
    SIZE = 50
    print(s[style])
    print('~'*SIZE)
    print(msg.center(SIZE))
    print('~'*SIZE, end='')
    print(s[0], end='')

    

# main program
try:
    while True:
        header('Help system PyHELP', 1)
        command = input('\nEnter function > ')
        if command.upper() == 'END':
            break
        else:
            special_help(command)
except:
    pass
finally:
    header('Good Bye', 3)
    print()
