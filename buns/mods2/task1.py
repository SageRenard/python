ab = input("Введите числа через запятую и пробел:")
ind1 = ab.find(", ")
a = int(ab[:ind1])
b = int(ab[ind1+1:])
s = a % b
print(s)
