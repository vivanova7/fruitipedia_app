from django.core.validators import MinLengthValidator
from django.db import models

from fruit_app.fruits import custom_validators


# Create your models here.
class Profile(models.Model):
    MAX_LEN_FN = 25
    MIN_LEN_FN = 2

    MAX_LEN_LN = 35
    MIN_LEN_LN = 1

    MAX_LEN_EMAIL = 40

    MAX_LEN_PASSWORD = 20
    MIN_LEN_PASSWORD = 8

    DEFAULT_AGE = 18

    first_name = models.CharField(
        max_length=MAX_LEN_FN,
        validators=(MinLengthValidator(MIN_LEN_FN), custom_validators.validate_first_letter),
        null=False,
        blank=False,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LN,
        validators=(MinLengthValidator(MIN_LEN_LN), custom_validators.validate_first_letter),
        null=False,
        blank=False,
        verbose_name='Last Name'
    )

    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators=(MinLengthValidator(MIN_LEN_PASSWORD),),
        null=False,
        blank=False,
        help_text="*Password length requirements: 8 to 20 characters"
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=True,
        default=DEFAULT_AGE,
    )