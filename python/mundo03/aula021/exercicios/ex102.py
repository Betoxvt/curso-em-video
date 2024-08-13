# Factorial function
# Do a program and create a function factorial() that receives two parameters: first identifies the number to calculate and second, called "show", is a boolean type indicating if the factorial calculation process will be shown.
def factorial(number, show=False):
    """
    -> Calculates a number factorial
    :param number: The positive integer number to calculate.
    :param show: (optional) Show or not the calculation process.
    :return: The factorial value for number.
    """
    for value in range(number, 1, -1):
        if show:
            print(f'{value} x ', end='')
        number *= value - 1
    print('1 = ', end='')
    return number
    
 
 # Main program   
print(factorial(6, True))
# help(factorial)

# Teacher Guanabara solution:
# def fatorial(n, show=False):
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
#         f *= c
#     return f
