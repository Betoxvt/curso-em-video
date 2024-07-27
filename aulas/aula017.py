# Compound variables — List (part 1)
# Lists are mutable, you can add, remove, or modify objects in a list.
# A list is written inside [ ]

# list.append(x) add x at the end of list
# list.insert(0,y) add y and place it at position [0]

# del list[3] deletes the object at position [3] from the list
# lanche.pop(3) same as above, but () removes the last
# lanche.remove(x) deletes x from the list
# after the removal of an object the list get re-arranged.

# Lists can be created using the range and list functions.
# Ex: values = list(range(4, 11))   [4, 5, 6, 7, 8, 9, 10]
# list.sort() organized
# list.sort(reverse=True) organized in reverse.

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
# num.remove(7)  # [5, 7, 3, 2] removes first object "7"
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
# print(f'This list has {len(num)} objects.')
#
# print('New list')
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
# print('End of list reached.')
#
# print('New list')
# values2 = list()
# for cont in range(0, 5):
#     values2.append(int(input('Enter a value: ')))
# for c, v in enumerate(values2):
#     print(f'At position {c} we have the value {v}!')
# print('End of list reached.')
# print(values2)

print('New list')
a = [2, 3, 4, 7]
b = a  # When we match one list with another, python creates a connection between them.
b[2] = 8  # This changes the number in both lists!
print(f'A list: {a}')
print(f'B list: {b}')
b = a[:]  # To make a copy that has no connection.
b[2] = 4  # Now this changes only b
print(f'A list: {a}')
print(f'B list: {b}')
