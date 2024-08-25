# Python deeper functions
# Rewrite function readInt() we did at ex104, including now the possibility to type in an invalid number type.
# Since we are at it, also create a function readFloat() with the same functionality.

def readInt():
    valid_input = False
    while not valid_input:
        try:
            msg = str(input('Type an integer: '))
            value = int(msg)
            valid_input = True
        except (ValueError, TypeError):
            print('\033[0;31mERROR:type a valid integer number.\033[m')
        except KeyboardInterrupt:
            value = 0
            print('\033[0;31mUser did not want to type this number.\033[m')
            break
    return value


def readFloat():
    valid_input = False
    while not valid_input:
        try:
            msg = str(input('Type a real: '))
            value = float(msg)
            valid_input = True
        except (ValueError, TypeError):
            print('\033[0;31mERROR:type a valid real number.\033[m')
        except KeyboardInterrupt:
            value = 0
            print('\033[0;31mUser did not want to type this number.\033[m')
            break
    return value

integer = readInt()
real = readFloat()
print(f'Integer typed value was {integer} and Real typed value was {real}.')
