# A special print
# Make a program with a function called write() that receives any text as parameter and show a message with dynamic size.
def write(txt):
    print('~'*((len(txt))+4))
    print(txt.center(len(txt)+4))
    print('~'*((len(txt))+4))

while True:
    write(input('Enter text: '))
    ans = input('Continue? [Y/N]: ').strip().upper()[0]
    if ans == 'N':
        break