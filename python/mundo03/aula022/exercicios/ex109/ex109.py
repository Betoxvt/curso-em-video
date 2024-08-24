# Modify created functions from ex107 so they can accept one more parameter informing if the value returned should be formated by 
# function coin() developed at ex108.
import coin

p = float(input('Enter price: $'))
print(f'The double of {coin.coin(p)} is {coin.double(p, False)}')
print(f'The half of {coin.coin(p)} is {coin.half(p)}')
print(f'Increasing 10%, we have {coin.increase(p,10, False)}')
print(f'Decreasing 15%, we have {coin.decrease(p,15)}')