# Formating coins
# Adapt ex107, creating an adictional function called coin() able to show values in monetary format.
import coin

p = float(input('Enter price: $'))
print(f'The double of {coin.coin(p)} is {coin.coin(coin.double(p))}')
print(f'The half of {coin.coin(p)} is {coin.coin(coin.half(p))}')
print(f'Increasing 10%, we have {coin.coin(coin.increase(p,10))}')
print(f'Decreasing 15%, we have {coin.coin(coin.decrease(p,15))}')
