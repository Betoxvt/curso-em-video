# Greater value finding function
# Create a program with a function called greater(), this will receive multiple parameters with integral values.
# Your program has to analyse all values and show which is higher.

def greater(* num):
    from time import sleep
    print('-='*30)
    print('Analyzing data...')
    sleep(0.6)
    for v in num:
        print(v, end=' ', flush=True)
        sleep(0.6)
    print(f'- The total of {len(num)} numbers.')
    sleep(0.6)
    print(f'The highest value informed is {max(num)}')
    sleep(1)


greater(4, 5, 3, 2)
greater(2, 2, 1, 0, 5, 2, 1)
greater(-1, 0, -2)