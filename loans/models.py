from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from .utils import check_loan_approval

def validate_amount(value):
    if value > 1000000:
        raise ValidationError('El monto solicitado no puede superar un millón.')

class LoanRequest(models.Model):
    dni = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex='^\d{1,8}$',
                message='El DNI debe ser un número con un máximo de 8 dígitos.'
            )
        ],
        error_messages={
            'max_length': 'El DNI debe tener un máximo de 8 caracteres.',
            'blank': 'El campo DNI no puede estar vacío.',
        }
    )
    full_name = models.CharField(
        max_length=255,
        error_messages={
            'blank': 'El campo Nombre y Apellido no puede estar vacío.',
        }
    )
    gender = models.CharField(
        max_length=10,
        error_messages={
            'blank': 'El campo Género no puede estar vacío.',
        }
    )
    email = models.EmailField(
        validators=[
            EmailValidator(
                message='Por favor, introduce una dirección de correo electrónico válida.'
            )
        ],
        error_messages={
            'invalid': 'Por favor, introduce una dirección de correo electrónico válida.',
            'blank': 'El campo Email no puede estar vacío.',
        }
    )
    amount = models.DecimalField(
        max_digits=9, 
        decimal_places=2,
        validators=[validate_amount],
        error_messages={
            'max_decimal_places': 'El monto solicitado no puede tener más de 2 decimales.',
            'blank': 'El campo Monto no puede estar vacío.',
        }
    )
    created_at = models.DateTimeField(default=timezone.now)
    loan_status = models.CharField(
        max_length=10, 
        blank=True, 
        null=True,
    )

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.loan_status = check_loan_approval(self.dni)
        super().save(*args, **kwargs)