# Counter function
# Make a program with function called counter() that receives 3 parameters:
# Start, End, Step and do the counting.
# Your program has to realize 3 countings through created function
# a) From 1 to 10, 1 by 1;
# b) From 10 to 0, 2 by 2;
# c) Custom

def counter(start, end, step):
    from time import sleep
    for c in range (0,3):
        if c == 0:
            start = 1
            end = 10
            step = 1
        elif c == 1:
            start = 10
            end = 0
            step = 2
        else:
            print('-='*25)
            print('Now it is your time to customize the counting!')
            start = int(input('Start: '))
            end = int(input('End: '))
            step = int(input('Step: '))
        print('-='*25)
        print(f'Counting from {start} to {end}, {step} by {step}')
        if start < end:
            while start <= end:
                print(start, end=' ', flush=True)
                start += step
                sleep(0.6)
            print('End!')
            sleep(0.6)
        elif start > end:
            while start >= end:
                print(start, end=' ', flush=True)
                start -= step
                sleep(0.6)
            print('End!')
            sleep(0.6)
        else:
            print(start, end=' ', flush=True)
            print('End!')
            sleep(0.6)

# Main script
counter(0,0,0)
