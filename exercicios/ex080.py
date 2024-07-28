# List sorted directly from input
# Create a program where the user can enter five numeric values and register them in a list,
# already at the correct ascending position (without using sort()).
# At the end, show the sorted list on screen.
_list = list()
for i in range(0, 5):
    v = int(input('Enter a value: '))
    if i == 0 or v >= _list[-1]:
        _list.append(v)
        print('Added at the end of the list.')
    elif v < _list[0]:
        _list.insert(0, v)
        print('Added at position 0.')
    elif _list[0] <= v < _list[1]:
        _list.insert(1, v)
        print('Added at position 1.')
    elif _list[1] <= v < _list[2]:
        _list.insert(2, v)
        print('Added at position 2.')
    elif _list[2] <= v < _list[3]:
        _list.insert(3, v)
        print('Added at position 3.')
print(_list)
