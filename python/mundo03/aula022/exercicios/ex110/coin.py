def summary(n, i=5, d=5):
    print('-'*32)
    print('VALUE SUMMARY'.center(32))
    print('-'*32)
    print(f'Analyzed price:\t\t{coin(n)}')
    print(f'Double price:\t\t{double(n)}')
    print(f'Half price:\t\t{half(n)}')
    print(f'{i}% increase:\t\t{increase(n, i)}')
    print(f'{d}% decrease:\t\t{decrease(n, d)}')
    print('-'*32)


def increase(n, p=5, m=True):
    i = n + n*p/100
    if m == True:
        i = coin(i)
    return i


def decrease(n, p=5, m=True):
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


def coin(n=0, c='$'):
    m = f'{c}{n:.2f}'
    return m
