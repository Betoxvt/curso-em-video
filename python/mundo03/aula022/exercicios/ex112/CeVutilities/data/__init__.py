def readMoney(msg='Enter price: $'):
    error = '\033[;31mOnly monetary values please\033[m'
    data = input(msg).strip().replace(',','.').split('.')
    while len(data) < 1 or len(data) > 2:
        print(error)
        data = input(msg).strip().replace(',','.').split('.')
    if len(data) == 1:
        while data[0].isnumeric() == False:
            print(error)
            data = input(msg).strip().split(',')
        money = float(data[0])
    if len(data) == 2:
        while data[0].isnumeric() == False or data[1].isnumeric() == False:
            print(error)
            data = input(msg).strip().replace(',','.').split('.')
        money = float('.'.join(data))
    return money
        

# Teacher Guanabara solution
# def readMoney(msg='Enter price: $'):
#     valid = False
#     while not valid:
#         data = input(msg).replace(',','.').strip()
#         if data.isalpha() or data == '':
#             print(f'\033[0;31mERROR: \"{data}\" is not a valid price!\033[m')
#         else:
#             valid = True
#             return float(data)
        