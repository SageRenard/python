input_filename = input("Введите имя файла для чтения: ")

with open(input_filename, 'r', encoding='utf-8') as file:
    text = file.read()

    letter_count = {}
    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    output_filename = input("Введите имя файла для записи статистики: ")

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1])

        for char, count in sorted_letter_count:
            output_file.write(f"{char}: {count}\n")
