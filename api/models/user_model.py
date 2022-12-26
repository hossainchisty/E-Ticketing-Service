from django.db import models
from django.contrib.auth.models import AbstractUser
from api.manager import UserManager

from utils.options import IdentificationTypeOptions


class CustomUser(AbstractUser):
    """ Custom user model."""
    username = None
    USERNAME_FIELD = 'mobile_number'
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    identification_type = models.CharField(
        max_length=20,
        choices=IdentificationTypeOptions.choices,
        help_text='Select a valid identification type.')
    identification_number = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    objects = UserManager()
