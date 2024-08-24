# Inside CeVutilities package we created on ex111, create a functions in data module called readMoney() capable to work like an input(), but with data validation to accept only monetary values.
from CeVutilities import data
from CeVutilities import coin

p = data.readMoney()
coin.summary(p, 10, 10)