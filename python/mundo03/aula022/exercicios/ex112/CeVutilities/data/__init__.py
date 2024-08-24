def readMoney():
    data = input('Enter price: $').strip().replace(',','.').split('.')
    while len(data) < 1 or len(data) > 2:
        print('Only monetary values please')
        data = input('Enter price: $').strip().replace(',','.').split('.')
    if len(data) == 1:
        while data[0].isnumeric() == False:
            print('Only monetary values please')
            data = input('Enter price: $').strip().split(',')
        money = float(data[0])
    if len(data) == 2:
        while data[0].isnumeric() == False or data[1].isnumeric() == False:
            print('Only monetary values please')
            data = input('Enter price: $').strip().replace(',','.').split('.')
        money = float('.'.join(data))
    return money
        
