a = int(input("Введите основание: "))

n = int(input("Введите степень: "))

def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        power = fast_power(a, n // 2)
        return power * power
    else:
        return a * fast_power(a, n - 1)


print(fast_power(a, n))
