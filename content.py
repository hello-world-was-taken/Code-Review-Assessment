def calculateArea(radius):
    if radius < 0:
        return 3.14 * (-1*radius)**2
    return 3.14 * radius ** 2

def divide_numbers(a, b):
    return a / b

def get_square(numbers):
    square = []
    for number in numbers:
        squares.append(number ** 2)
    return square

def get_cubes(numbers):
    cubes = []
    for number in numbers:
        cubes.append(number ** 3)
    return cubes

my_numbers = [1, 2, 3, 4, 5]
squares = get_square(my_numbers)
cubes = get_cubes(my_numbers)

count = 0

def multiply(x, y):
    return x * y

def increment_count():
    global count
    count += 1

increment_count()
print(count)

