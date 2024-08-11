# Lists with odd and even numbers
# Create a program that the user can enter seven numeric values and register them in one numbers_list that keeps
# Odds and even numbers separated. At the end, print the data in ascending order.
numbers = [[], []]
for i in range(0, 7):
    num = int(input('Enter a number: '))
    if num % 2 != 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)
numbers[0].sort()
numbers[1].sort()
print('—'*50)
print(f'Numbers list: {numbers}')
print(f'Odd numbers: {numbers[0]}')
print(f'Even numbers: {numbers[1]}')
