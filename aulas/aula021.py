# Functions (part 2)

# - Interactive Help
# - docstrings
# - Optional arguments
# - Variable scope
# - Results return


# > Interactive Help
# - function help()


help(input)
print(input.__doc__)
print('-='*20)


# > docstring
# - To add information in help()
# - On the next line, below def function use triple quotes

def counter(b, e, s):
    """
    -> Do a counting and shows on screen.
    :param b: beginning
    :param e: ending
    :param s: step
    :return: none
    """
    c = b
    while c <= e:
        print(c, end='...')
        c += s
    print('END')


counter(2, 10, 2)
print('-='*20)


# > Optional arguments
# - Default values for the parameters, used if none is informed.
# - If an optional parameter is not defined, and the user don't inform an argument/value, causes error


def _sum(a=0, b=0, c=0):
    """
    -> Do a sum, up to 3 values and shows on screen.
    :param a: first value
    :param b: second value
    :param c: third value
    """
    s = a + b + c
    print(f'The sum is {s}')


_sum(2, 3, 4)
print('-='*20)


# > Variable scope
# = Place where the variable exist and place where it doesn't exist
# - Global scope: accessed from all the code, including functions, defined outside functions or classes
# - Local scope: defined inside a function and only accessed there
# - So it is possible to have two variables with the same name but different values, because of scope.
# - This concept also applies to libraries.


def function():
    n1 = 4
    print(f'n1 inside function is {n1} "Local Scope"')


n1 = 2
function()
print(f'Outside, n1 is {n1} "Global Scope"')
print('-=' * 20)


# You can also tell the function to not create a local variable and use the global instead using global <var>,
# this way you can modify the variable inside the function to affect the global scope

def test(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A inside is {a}')
    print(f'B inside is {b}')
    print(f'C inside is {c}')


a = 5
test(a)
print(f'A outside is {a}')
print('-=' * 20)


# Returning values

def _sum(a=0, b=0, c=0):
    s = a + b + c
    return s


print(_sum(2, 3, 4))
result1 = _sum(2, 3, 4)
result2 = _sum(2, 2)
result3 = _sum(3)
print(f'My calculations are {result1}, {result2}, {result3}')
print('-='*20)
