num = input()
if num.isdigit():
    num = int(num)
    print(f"{bin(num)[2:]}, {oct(num)[2:]}, {hex(num)[2:]}")
else:
    print("Неверный ввод")
