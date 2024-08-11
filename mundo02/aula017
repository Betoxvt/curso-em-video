# Compound variables — List (part 1)
# Lists are mutable, you can add, remove, or modify elements in a numbers_list.
# A numbers_list is written inside [ ]

# numbers_list.append(x) add x at the end of numbers_list
# numbers_list.insert(0,y) add y and place it at position [0]

# del numbers_list[3] deletes the element at position [3] from the numbers_list.
# lanche.pop(3) same as above, but () removes the last element.
# lanche.remove(x) deletes x from the numbers_list.
# after the removal of an element the numbers_list get re-arranged.

# Lists can be created using the range and numbers_list functions.
# Ex: values = numbers_list(range(4, 11))   [4, 5, 6, 7, 8, 9, 10]
# numbers_list.sort() organized
# numbers_list.sort(reverse=True) organized in reverse.

# num = [2, 5, 9, 1]
# num[2] = 3  # [2, 5, 3, 1]
# # num[4] = 7  # error
# num.append(7)  # [2, 5, 3, 1, 7]
# num.sort()  # [1, 2, 3, 5, 7]
# num.sort(reverse=True)  # [7, 5, 3, 2, 1]
# num.insert(2, 0)  # [7, 5, 0, 3, 2, 1]
# num.pop()  # [7, 5, 0, 3, 2]
# num.pop(2)  # [7, 5, 3, 2]
# num.insert(2, 7)  # [7, 5, 7, 3, 2]
# num.remove(7)  # [5, 7, 3, 2] removes first element "7"
# # num.remove(4)  # error
# if 4 in num:
#     num.remove(4)
# else:
#     print('Could not find number 4')
# if 5 in num:
#     num.remove(5)
# else:
#     print('Could not find number 5')
# print(num)
# print(f'This numbers_list has {len(num)} elements.')
#
# print('New numbers_list')
# values = []
# values.append(5)
# values.append(9)
# values.append(4)
# print(values)
# for v in values:
#     print(f'{v}...', end='')
# print('')
# for c, v in enumerate(values):
#     print(f'At position {c} we have the value {v}!')
# print('End of numbers_list reached.')
#
# print('New numbers_list')
# values2 = numbers_list()
# for cont in range(0, 5):
#     values2.append(int(input('Enter a value: ')))
# for c, v in enumerate(values2):
#     print(f'At position {c} we have the value {v}!')
# print('End of numbers_list reached.')
# print(values2)

print('New numbers_list')
a = [2, 3, 4, 7]
b = a  # When we match one numbers_list with another, python creates a connection between them.
b[2] = 8  # This changes the number in both lists!
print(f'A numbers_list: {a}')
print(f'B numbers_list: {b}')
b = a[:]  # To make a copy that has no connection.
b[2] = 4  # Now this changes only b
print(f'A numbers_list: {a}')
print(f'B numbers_list: {b}')

names = ["Sam", "Peter", "James", "Julian", "Ann"]
print(*names, sep=", ")  # '*' shows the numbers_list with no []. Sep prints the string between the elements.
# output: Sam, Peter, James, Julian, Ann
