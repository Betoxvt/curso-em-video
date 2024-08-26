# Create a small module system to register persons by their name and age in a simple text file.
# This system onle has two options: register new person and list all people registered.
from ex115_system import system as sy

sys_on = True
while sys_on:
    try:
        sy.main_menu()
        option = sy.options()
        if option == 1:
            sy.see()
        if option == 2:
            pData = sy.readPerson()
            sy.register(pData)
        if option == 3:
            sy.exit()
            break
    except KeyboardInterrupt:
        sy.color(' User forced exit')
        break
