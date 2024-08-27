def color(msg='', c=1):
    if c == 1:
        print(f'\033[31m{msg}\033[m')  # RED
    if c == 2:
        print(f'\033[32m{msg}\033[m')  # GREEN


def readInt(msg):
    while True:
        try:
            value = int(input(msg))
        except (ValueError, TypeError):
            color('ERROR:type a valid integer number.')
            continue
        else:
            return value


def line(tam=42):
    return '-' * tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())

def menu(List):
    header('MAIN MENU')
    c = 1
    for item in List:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opt = readInt('\033[32mEnter your option: \033[m')
    return opt