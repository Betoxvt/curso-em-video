# More about matrix in python
# Improve the previous exercise, printing at the end:
# A) The sum of all entered evens.
# B) The sum of the numbers at the third column.
# C) The highest number in the second row.
matrix = [[], [], []]
for r in range(0, 3):
    for c in range(0, 3):
        matrix[r].append(int(input(f'Enter value for [{r}, {c}]: ')))
print('—'*40)
for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[r][c]:^5}]', end='')
    print()
print('—'*40)
evsum = tcsum = srhigh = 0
for r in range(0, 3):
    for c in range(0, 3):
        if matrix[r][c] % 2 == 0:
            evsum += matrix[r][c]
        if c == 2:
            tcsum += matrix[r][c]
        if r == 1 and c == 0:
            srhigh = matrix[r][c]
        elif r == 1 and matrix[r][c] > srhigh:
            srhigh = matrix[r][c]
print(f'The even numbers add up to {evsum}.')
print(f'The third column numbers add up to {tcsum}')
print(f'The second row highest number is {srhigh}')
