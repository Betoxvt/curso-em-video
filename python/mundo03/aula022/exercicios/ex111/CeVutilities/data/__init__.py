def readMoney():
    data = input('Enter price: $').strip().replace(',', '.')
    while data.isnumeric() == False:
        print('Only monetary values please')
        data = input('Enter price: $').strip().replace(',', '.')
    money = float(data)
    return money
        
