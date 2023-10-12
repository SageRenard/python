num = input()
number = ''.join([char for char in num if char.isdigit() or char == '+'])
print(number)
