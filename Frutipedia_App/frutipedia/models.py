from django.core.validators import MinLengthValidator
from django.db import models
from django.core import validators
from Frutipedia_App.frutipedia.validators import validate_profile_name,validate_fruit_name
# Create your models here.


class ProfileModel(models.Model):

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=25,
        validators=[MinLengthValidator(2), validate_profile_name],
        null=False,
        blank=False
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=35,
        validators=[MinLengthValidator(1), validate_profile_name],
        null=False,
        blank=False
    )

    email = models.EmailField(
        verbose_name='Email',
        max_length=40,
        null=False,
        blank=False
    )
    password = models.CharField(
        verbose_name='Password',
        max_length=20,
        validators=[MinLengthValidator(8)],
        null=False,
        blank=False
    )
    image_url = models.URLField(
        verbose_name='Image URL',
        null=True,
        blank=True
    )
    age = models.IntegerField(
        verbose_name='Age',
        default=18,
        blank=True,
        null=True
    )
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class FruitModel(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=30,
        validators=[MinLengthValidator(2), validate_fruit_name],
        null=False,
        blank=False
    )
    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Description',
        null=False,
        blank=False
    )
    nutrition = models.TextField(
        verbose_name='Nutrition',
        null=True,
        blank=True
    )