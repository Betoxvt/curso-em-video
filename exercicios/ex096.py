# Function - Area calculator
# Create a program that has a function called area(), receiving a rectangular land dimensions and show the land area.
def area(length, width):
    area = length * width
    print(f'The area of a land {length} X {width} is {area}m²')


area(float(input('Length (m): ')), float(input('Width (m): ')))
