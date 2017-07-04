from django.core.exceptions import ValidationError

from eventex.subscriptions.cpf_validator import cpf_is_valid


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CFP deve conter apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')

    if cpf_is_valid(value):
        raise ValidationError('Dígito do CPF não confere, verificar digitação', 'invalid')