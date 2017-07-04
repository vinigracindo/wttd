def cpf_is_digits(value):
    """
    This function receives the Brazilian CPF and returns True if it contains only digits or False if not.
    :param value: A string with the number of Brazilian CPF
    :return: True or False
    """
    if value.isdigit():
        return True
    return False


def cpf_has_correct_length(value):
    """
    This function receives the Brazilian CPF and returns True if the length of CPF is 11 or False if not.
    :param value: A string with the number of Brazilian CPF
    :return:
    """
    if len(value) != 11:
        return True
    return False


def cpf_is_valid(value):
    """
    This function receives the Brazilian CPF and returns True if the CPF is valid or False if not valid
    :param value: A string with the Brazilina CPF
    :return: True or False
    """

    value = [int(digit) for digit in value]
    intermediate = value[:9]
    list_values_to_calc = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    while len(intermediate) < 11:
        estimate = sum(x * y for (x, y) in zip(intermediate, list_values_to_calc)) % 11
        intermediate.append((0, 11 - estimate)[estimate >= 2])
        list_values_to_calc.insert(0, 11)

    if value[-2:] != intermediate[-2:]:
        return True
    else:
        return False
