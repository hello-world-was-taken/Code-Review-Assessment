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