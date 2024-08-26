def title(msg=''):
    print('-'*50)
    print(msg.center(50))
    print('-'*50)


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
                 print('\033[31m Please enter a valid option (1 - 3)\033[m')
        except (ValueError, TypeError):
             print('\033[31mAn error occurred: Please enter a valid integer number\033[m')
        except KeyboardInterrupt:
            print('\033[31mUser forced exit.\033[m')
            break
        except Exception as e:
            print(f'\033[31mAn error occurred: {type(e).__name__}\033[m')


def readPerson():
    while True:
        try:
            name = str(input('Name: ')).strip().title()
            age = int(input('Age: '))
            if len(name) == 0:
                print('\033[31mPlease enter a name.\033[m')
            else:
                return [name, age]
        except (ValueError, TypeError):
            print('\033[31mAn error occurred:<Age> is an integer number]\033[m')
        except KeyboardInterrupt:
            print('\033[31mUser forced exit.\033[m')
            break
        except Exception as e:
            print(f'\033[31mAn error occurred: {type(e).__name__}\033[m')


def exit():
    title('Thank you for using our system. Good Bye.')


def register(pData):
    with open("./ex115_system/data/people.txt", "a") as file:
        file.write(f'{pData[0]:.<40}{pData[1]:.>6} y/o\n')


def see():
    with open("./ex115_system/data/people.txt", "r") as file:
        lines = file.readlines()
        print('-'*50)
        for line in lines:
            print(line.strip())
