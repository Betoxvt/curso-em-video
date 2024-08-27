from ex115.lib.interface import *
from ex115.lib.archive import *
from time import sleep

file = './ex115/persons.txt'

if fileExists(file):
    color('Archive found', 2)
else:
    color('Archive not found!', 1)
    createFile(file)

while True:
    try:
        answer = menu(['See Persons Registered', 'Register New Person', 'Exit System'])
        if answer == 1:
            see()
        elif answer == 2:
            header('REGISTER NEW PERSON')
            registerPerson()
        elif answer == 3:
            header('Leaving System. Thank you for using.')
            break
        else:
            print('\033[31mERROR! Enter a valid option!\033[m')
        sleep(2)
    except KeyboardInterrupt:
        color('\nUser forced exit')
        break