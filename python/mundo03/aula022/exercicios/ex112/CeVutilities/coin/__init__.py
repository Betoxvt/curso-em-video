def summary(n, i, d):
    print('-'*30)
    print('VALUE SUMMARY'.center(30))
    print('-'*30)
    print(f'{'Analyzed price:':<20}{coin(n)}')
    print(f'{'Double price:':<20}{double(n)}')
    print(f'{'Half price:':<20}{half(n)}')
    print(f'{i}% increase:       {increase(n, i)}')
    print(f'{d}% decrease:       {decrease(n, d)}')
    print('-'*30)


def increase(n, p, m=True):
    i = n + n*p/100
    if m == True:
        i = coin(i)
    return i


def decrease(n, p, m=True):
    d = n - n*p/100
    if m == True:
        d = coin(d)
    return d


def double (n, m=True):
    db = n * 2
    if m == True:
        db = coin(db)
    return db


def half(n, m=True):
    h = n / 2
    if m == True:
        h = coin(h)
    return h


def coin(n):
    m = f'${n:.2f}'
    return m
