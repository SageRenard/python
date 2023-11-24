import re

def is_valid_date(date_string):
    """
    Проверяет, является ли входная строка корректной датой в одном из заданных форматов.

    Args:
    date_string (str): Строка, представляющая дату.

    Returns:
    bool: True, если строка представляет собой корректную дату, иначе False.

    >>> is_valid_date("20 января 1806")
    True
    >>> is_valid_date("1924, July 25")
    True
    >>> is_valid_date("26/09/1635")
    True
    >>> is_valid_date("3.1.1506")
    True
    >>> is_valid_date("25.08-1002")
    False
    >>> is_valid_date("декабря 19, 1838")
    False
    >>> is_valid_date("8.20.1973")
    False
    >>> is_valid_date("Jun 7, -1563")
    False
    >>> is_valid_date("31 февраля 2023")
    False
    >>> is_valid_date("31 июня 2015")
    False
    """
    pattern = r"^((?:[1-9]|[1-2]\d|30|31)/(?:[1-9]|0[1-9]|10|11|12)/\d{4})$|^((?:[1-9]|[1-2]\d|30|31)\.(?:[1-9]|0[1-9]|10|11|12)\.\d{4})$|^(\d{1,4}\,\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря|January|February|March|April|May|June|July|August|September|October|November|December)\s(?:[1-9]|[1-2]\d|30|31))$|^((?:[1-9]|[1-2]\d|30|31)\s(?:января|марта|мая|июля|августа|октября|декабря|January|March|May|July|August|October||December)\s\d{1,4})$|^((?:[1-9]|[1-2]\d|30)\s(?:|апреля|июня|сентября|ноября|April|June|September|November|)\s\d{1,4})$|^((?:[1-9]|[1]\d|2[0-8]|)\s(?:февраля|February)\s\d{1,4})$"
    return bool(re.match(pattern, date_string))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()

    if result.failed == 0:
        print("Все тесты прошли успешно!")
    else:
        print("Тесты не прошли.")

# Примеры корректных дат
print(is_valid_date("20 января 1806"))               # True
print(is_valid_date("1924, July 25"))                 # True
print(is_valid_date("26/09/1635"))                 # True
print(is_valid_date("3.1.1506"))                # True


print()

# Примеры некорректных дат
print(is_valid_date("25.08-1002"))                # False
print(is_valid_date("декабря 19, 1838"))          # False
print(is_valid_date("8.20.1973"))                 # False
print(is_valid_date("Jun 7, -1563"))              # False
print(is_valid_date("31 февраля 2023"))           # False
print(is_valid_date("31 июня 2015"))   
