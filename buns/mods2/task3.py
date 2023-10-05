abc = input("Введите числа через запятую и пробел:")
ind1 = abc.find(", ")
a = int(abc[:ind1])
ind2 = abc.find(", ", ind1+1)
b = int(abc[ind1+1:ind2])
c = int(abc[ind2+1:])

assert -1000 <= a <= 1000, "Неверное значение a"
assert -1000 <= b <= 1000, "Неверное значение b"
assert -1000 <= c <= 1000, "Неверное значение c"

if a <= b <= c:
    print(b)
elif c <= b <= a:
    print(b)
elif b <= a <= c:
    print(a)
elif c <= a <= b:
    print(a)
else:
    print(c)

