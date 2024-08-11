# Functions (Part 1)
# > Routine(print() len() input() int() float()) are functions
# Functions can be made, like "line()", use a parameter.

""" def line():
    print('-'*30)


line()
print('STUDENTS SYSTEM'.center(30))
line()

def title(txt):
    line()
    print(txt.center(30))
    line()


title('PYTHON IS VERY GOOD')

title(input('Enter title: ')) """

# You can have multiple parameters in the function

""" def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# main program
soma(4, 5)
soma(a=4, b=5)
soma(b=4, a=5) # This is OK you can switch places if its declared
# soma(b=4, 5) # Error, can't figure out if one argument is not declared
# soma(3, 9, 5) # Error, more than 2 arguments """

# Python allows "packing arguments"
# This way, a function to accept an arbitrary number of arguments.
# * before the parameter.

# Working with tuples

""" def count(* num):
    for v in num:
        print(v, end=' ')
    print('END!')
    size = len(num)
    print(f'Values entered are {num} and it has {size} numbers in total')


count(2, 1, 7)
count(8, 8)
count(4, 4, 7, 2) """

# Working with lists/arrays

""" def double(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


values = [7, 2, 5, 0, 4]
double(values)  # This will change the numbers_list
print(values)  # [14, 4, 10, 0, 8] """

# Unpacking

def soma(* values):
    s = 0
    for num in values:
        s += num
    print(f'Adding values {values} we have {s}')

soma(5, 2)
soma(2, 9, 4)