# Draw and sum functions
# Do a program with a list "numbers" and 2 functions called draws() and sumEven(). First will draw 5 numbers inside the list and the second will show the sum between the even drawn values.
from random import randint
from time import sleep
numbers = []

def draw(*num):
    print('Drawing five numbers...', end=' ')  
    for c in range(0, 5):
        numbers.append(randint(1,100))
        print(numbers[c], end=' ', flush=True)
        sleep(0.6)
    print('DONE!')


def sumEven(*num):
    sum = 0
    for v in numbers:
        if v % 2 == 0:
            sum += v
    print(f'The sum of even values in {numbers} is {sum}.')


draw()
sumEven()