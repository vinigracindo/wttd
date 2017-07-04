def cpf_is_valid(value):
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
