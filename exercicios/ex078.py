# Largest and smallest values in a list
# Create a program that reads 5 numeric values and saves them in a list.
# At the end, show the largest, and the smallest values entered and their respective positions in the list.
# Class method:
numbers_list = []
largest = 0
smallest = 0
for c in range(0, 5):
    numbers_list.append(int(input(f'Enter a value for position {c}: ')))
    if c == 0:
        largest = smallest = numbers_list[c]
    else:
        if numbers_list[c] > largest:
            largest = numbers_list[c]
        if numbers_list[c] < smallest:
            smallest = numbers_list[c]
print('=-' * 30)
print(f'You entered the values {numbers_list}')
print(f'The largest value is {largest} at positions ', end='')
for i, v in enumerate(numbers_list):
    if v == largest:
        print(f'{i}... ', end='')
print(f'\nThe smallest value is {smallest} at positions ', end='')
for i, v in enumerate(numbers_list):
    if v == smallest:
        print(f'{i}... ', end='')
print()

# My solution
# num = list()
# largest = [0, 0]
# smallest = [0, 0]
# for i in range(0, 5):
#     num.append(int(input(f'Enter a number for position {i}: ')))
#     if i == 0 or num[i] > largest[0]:
#         largest = [num[i], i]
#     if i == 0 or num[i] < smallest[0]:
#         smallest = [num[i], i]
#     if num[i] == largest[0]:
#         largest.append(i)
#     if num[i] == smallest[0]:
#         smallest.append(i)
# print('—' * 60)
# print(f'The list formed is {num}')
# print(f'The largest number is {largest[0]} at positions ', end='')
# for i in range(1, len(largest)):
#     if i > 1:
#         print(f'{largest[i]}... ', end='')
# print(f'\nThe smallest number is {smallest[0]} at positions ', end='')
# for i in range(1, len(smallest)):
#     if i > 1:
#         print(f'{smallest[i]}... ', end='')
