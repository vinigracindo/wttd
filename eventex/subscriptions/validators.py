from django.core.exceptions import ValidationError

from eventex.subscriptions.cpf_validator import cpf_is_valid, cpf_has_correct_length, cpf_is_digits


def validate_cpf(value):
    if not cpf_is_digits(value):
        raise ValidationError('CPF deve conter apenas números.', 'digits')

    if cpf_has_correct_length(value):
        raise ValidationError('CPF deve ter 11 números.', 'length')

    if cpf_is_valid(value):
        raise ValidationError('Dígito do CPF não confere, verificar digitação', 'invalid')
