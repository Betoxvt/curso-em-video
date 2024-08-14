# Validating data entry in Python
# Create a program that has the function readInt(), it will work in a way similar to function input(), but also validating to accept only integer numeric values.
# Ex.: n = readInt('Enter a number: ')
def readInt(num):
    while True:
        global integer
        value = str(input(f'{num}'))
        if value.isnumeric():
            integer = value
            break
        else:
            print('\033[31mERROR! Please enter an integer number.\033[m')

# Main program
number = readInt("Enter a number: ")
print(f'You just entered number {integer}')


# Teacher Guanabara solution - returns the value, less simple but more reliable (using same variable)
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
    

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Vocẽ acabou de digitar o número {n}')
