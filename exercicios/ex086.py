# Matrix in python
# Create a program that creates a 3x3 dimensions matrix and fill it with data entered from the keyboard.
# Finally, print the matrix on screen, properly formatted.
matrix = [[], [], []]
for r in range(0, 3):
    for c in range(0, 3):
        matrix[r].append(int(input(f'Enter a value for [{r}, {c}]: ')))
print('—'*50)
for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[r][c]:^5}]', end='')
    print()
