from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')

    value = [int(digit) for digit in value]
    intermediate = value[:9]
    list_values_to_calc = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    while len(intermediate) < 11:
        estimate = sum([x * y for (x, y) in zip(intermediate, list_values_to_calc)]) % 11
        intermediate.append((0, 11 - estimate)[estimate >= 2])
        list_values_to_calc.insert(0, 11)

    if value[-2:] != intermediate[-2:]:
        raise ValidationError('Dígito do CPF não confere, verificar digitação')
