# Python modules exercice
# Create a module called coin.py with the functions: increase(), decreasce(), double() and half().
# Also a program importing those functions and using some of them.
import coin

p = float(input('Enter price: $'))
print(f'The double of {p} is {coin.double(p)}')
print(f'The half of {p} is {coin.half(p)}')
print(f'Increasing 10%, we have {coin.increase(p,10)}')
print(f'Decreasing 15%, we have {coin.decrease(p,15)}')
