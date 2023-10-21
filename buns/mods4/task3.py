a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

print(euclid(a, b))
