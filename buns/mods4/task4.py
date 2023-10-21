word = input("Введите слово: ")

def make_palindrome(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    middle_char = ''
    for char, count in char_count.items():
        if count % 2 != 0:
            odd_count += 1
            middle_char = char

    return odd_count <= 1, middle_char

def is_palindrome(word):
    make, middle_char = make_palindrome(word)
    if make:
        char_count = {}
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        palindrome = ''
        for char, count in char_count.items():
            palindrome += char * (count // 2)

        return palindrome + middle_char + palindrome[::-1]
    else:
        return "Невозможно составить палиндром"

print(is_palindrome(word))
