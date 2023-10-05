length = int(input("Введите длину стороны квадрата:"))

perimeter = 4 * length
square = length ** 2
diagonal = (2 * length ** 2) ** 0.5

print("{:.2f}, {:.2f}, {:.2f}".format(perimeter, square, diagonal))
