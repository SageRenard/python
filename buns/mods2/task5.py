def find_shifted_char(i, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_len = len(alphabet)

    if i.isalpha() and i.islower():
        i_index = alphabet.index(i)

        k_index = (i_index + n) % alphabet_len
        return alphabet[k_index]
    else:
        return "Некорректный символ"


ab = input("Введите данные через запятую и пробел:")
ind1 = ab.find(", ")
i = str(ab[:ind1])
n = int(ab[ind1 + 1:])

print(find_shifted_char(i, n))
