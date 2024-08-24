# Modules and packages
def factorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('Enter a value: '))
fact = factorial(num)
print(f'The factorial of {num} is {fact}')
