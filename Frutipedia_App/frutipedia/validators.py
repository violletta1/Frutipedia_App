from django.core import validators
from django.core.exceptions import ValidationError

def validate_profile_name(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a letter!")

def validate_fruit_name(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")