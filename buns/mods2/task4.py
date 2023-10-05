number = input("Введите число:")

if not number.isdigit() or int(number) <= 0:
    print("Неверный ввод")
else:
    num = int(number)
    binary = ""
    octal = ""
    hexadecimal = ""

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    num = int(number)
    while num > 0:
        octal = str(num % 8) + octal
        num //= 8

    num = int(number)
    while num > 0:
        remainder = num % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        num //= 16

    print(binary + ", " + octal + ", " + hexadecimal)
