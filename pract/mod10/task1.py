import re

def is_valid_password(password):
    """
    Проверяет, соответствует ли входной пароль всем заданным ограничениям.

    >>> is_valid_password("rtG&3FG#Tr^e")
    True

    >>> is_valid_password("a^A1@*@1Aa")
    True

    >>> is_valid_password("oF^a1D@y5%e6")
    True

    >>> is_valid_password("enroi#$*rkdeR#$*092uwedchf34tguv394h")
    True

    >>> is_valid_password("пароль")
    False

    >>> is_valid_password("password")
    False

    >>> is_valid_password("qwerty")
    False

    >>> is_valid_password("lOngPa$$W0Rd")
    False
    """

    # Пароль должен содержать только латинские символы, цифры и специальные символы ^$%@#&*
    if not re.match(r'^[a-zA-Z0-9^$%@#&*]+$', password):
        return False

    # Пароль должен состоять из не менее чем восьми символов
    if len(password) < 8:
        return False

    # Пароль должен содержать по крайней мере два латинских символа в нижнем регистре
    if len(re.findall(r'[a-z]', password)) < 2:
        return False

    # Пароль должен содержать по крайней мере одну цифру
    if len(re.findall(r'\d', password)) < 1:
        return False

    # Пароль должен содержать по крайней мере три различных специальных символа
    if len(set(re.findall(r'[^a-zA-Z0-9]', password))) < 3:
        return False

    # Проверка отсутствия символов ,.!?
    if re.search(r'[,\.\!\?]', password):
        return False
    return True 



if __name__ == "__main__":
    import doctest
    result = doctest.testmod()

    if result.failed == 0:
        print("Все тесты прошли успешно!")
    else:
        print("Тесты не прошли.")

print(is_valid_password("rtG&3FG#Tr^e"))  # True
print(is_valid_password("a^A1@*@1Aa"))    # True
print(is_valid_password("oF^a1D@y5%e6"))  # True
print(is_valid_password("enroi#$*rkdeR#$*092uwedchf34tguv394h"))  # True

print(is_valid_password("пароль"))         # False
print(is_valid_password("password"))        # False
print(is_valid_password("qwerty"))          # False
print(is_valid_password("lOngPa$$W0Rd"))    # False
