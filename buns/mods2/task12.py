telephone_number = input("Введите номер телефона: ")

continuous_number = telephone_number.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")

print(continuous_number)
