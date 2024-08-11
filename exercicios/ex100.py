# Draw and sum functions Do a program with a numbers_list "numbers" and 2 functions called draws() and sum_even().
# First will draw 5 numbers inside the numbers_list and the second will show the sum between the even drawn values.
from random import randint
from time import sleep


def draw(numbers_list):
    print('Drawing five numbers...', end=' ')
    for c in range(0, 5):
        numbers_list.append(randint(1, 100))
        print(numbers[c], end=' ', flush=True)
        sleep(0.6)
    print('DONE!')


def sum_even(numbers_list):
    sum = 0
    for v in numbers_list:
        if v % 2 == 0:
            sum += v
    print(f'The sum of even values in {numbers_list} is {sum}.')


numbers = list()
draw(numbers)
sum_even(numbers)
