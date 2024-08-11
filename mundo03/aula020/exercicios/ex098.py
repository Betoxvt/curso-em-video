# Counter function
# Make a program with function called counter() with 3 parameters:
# Start, End, Step and do the counting.
# Your program has to count 3 times through created function
# a) From 1 to 10, 1 by 1;
# b) From 10 to 0, 2 by 2;
# c) Custom
"""Did not have to write all inside the function"""


def counter(start, end, step):
    from time import sleep
    for c in range(0, 3):
        if c == 0:
            start = 1
            end = 10
            step = 1
        elif c == 1:
            start = 10
            end = 0
            step = 2
        else:
            print('-=' * 25)
            print('Now it is your time to customize the counting!')
            start = int(input('Start: '))
            end = int(input('End: '))
            step = int(input('Step: '))
        print('-=' * 25)
        print(f'Counting from {start} to {end}, {step} by {step}')
        if step < 0:
            step = -step
        if step == 0:
            print('Cant use "Step = 0", swapping for "Step = 1"')
            step = 1
        if start < end:
            for c in range(start, end + 1, step):
                print(c, end=' ', flush=True)
                sleep(0.6)
            print('End!')
            sleep(0.6)
        elif start > end:
            for c in range(start, end - 1, -step):
                print(c, end=' ', flush=True)
                sleep(0.6)
            print('End!')
            sleep(0.6)
        else:
            print(start, end=' ', flush=True)
            print('End!')
            sleep(0.6)


# Main script
counter(0, 0, 0)
