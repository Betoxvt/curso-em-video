# Python modules exercice
# Create a module called coin.py with the functions: increase(), decreasce(), double() and half().
# Also a program importing those functions and using some of them.
import coin

p = float(input('Enter price: $'))
print(f'The double of ${p:.2f} is ${coin.double(p):.2f}')
print(f'The half of ${p:.2f} is ${coin.half(p):.2f}')
print(f'Increasing 10%, we have ${coin.increase(p,10):.2f}')
print(f'Decreasing 15%, we have ${coin.decrease(p,15):.2f}')
