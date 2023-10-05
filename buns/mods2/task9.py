string = input()

glas = 0
sogl = 0

for letter in string:
    if letter.lower() in "аеёиоуыэюя":
        glas += 1
    elif letter.lower() in "бвгджзйклмнпрстфхцчшщ":
        sogl += 1

print(glas, sogl)
