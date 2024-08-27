from ex115.lib.interface import *


def fileExists(name):
    try:
        f = open(name, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def createFile(name):
    try:
        f = open(name, 'wt+')
        f.close()
    except Exception as e:
        color(f'A error ocurred: {e}')
    else:
        color(f'File path {name} created!', 2)
    

def registerPerson():
    while True:
        try:
            name = str(input('Name: ')).strip().title()
            if name.replace("'", "").replace(' ', '').isalpha():
                age = int(input('Age: '))
                if age < 150:
                    color(f'Name: {name} | Age: {age}', 2)
                else:
                    color('Age invalid, too old')
            else:
                color('Name invalid')
        except (ValueError, TypeError):
            color('An error occurred: <Age> type or value')
        except KeyboardInterrupt:
            color('User forced exit.')
            break
        else:
            try:
                with open('./ex115/persons.txt', "a") as file:
                    file.write(f'{name};{age}\n')
            except TypeError:
                color('This object is not subscriptable')
            else:
                color('Person registered with success!', 2)
                break
            finally:
                file.close()


def see():
    try:
        file = open('./ex115/persons.txt', 'rt')
    except FileNotFoundError:
        color('File not found')
    except Exception as e:
        color(f'Error reading file, {e}')
    else:
        header('LIST OF REGISTERED PERSONS')
        for line in file:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:.<30}{data[1]:.>8} y/o')
    finally:
        file.close()
