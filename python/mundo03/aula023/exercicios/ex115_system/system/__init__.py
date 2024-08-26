def title(msg=''):
    print('-'*50)
    print(msg.center(50))
    print('-'*50)

def color(msg='', c=1):
    if c == 1:
        print(f'\033[31m{msg}\033[m')
    if c == 2:
        print(f'\033[32m{msg}\033[m')


def main_menu():
        title('MAIN MENU')
        print('\033[33m[1] - \033[36mSee Persons List\033[m')
        print('\033[33m[2] - \033[36mRegister New Person\033[m')
        print('\033[33m[3] - \033[36mExit System\033[m')
        print('-'*50)


def options():
    OPTIONS = (1, 2, 3)
    while True:
        try:
            option = int(input('\033[33mSelect an option: \033[m'))
            if option in OPTIONS:
                 return option
            else:
                 color('Please enter a valid option (1, 2 or 3)')
        except (ValueError, TypeError):
             color('An error occurred: Not a valid input')


def readPerson():
    title('REGISTER NEW PERSON')
    while True:
        try:
            name = str(input('Name: ')).strip().title()
            if name.replace("'", "").replace(' ', '').isalpha():
                age = int(input('Age: '))
                if age < 150:
                    color(f'Saving {name} with {age} y/o', 2)
                    return [name, age]
                else:
                    color('Age invalid')
            else:
                color('Name invalid')
        except (ValueError, TypeError):
            color('An error occurred: <Age> type or value')


def exit():
    title('Thank you for using our system. Good Bye.')


def register(pData):
    try:
        with open("./ex115_system/data/people.txt", "a") as file:
            file.write(f'{pData[0]:.<40}{pData[1]:.>6} y/o\n')
            color('Person registered with success!', 2)
    except TypeError:
        color('This object is not subscriptable')



def see():
    with open("./ex115_system/data/people.txt", "r") as file:
        lines = file.readlines()
        title('LIST OF REGISTERED PEOPLE')
        for line in lines:
            print(line.strip())
