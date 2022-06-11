from django.db import models
from django.contrib.auth.models import AbstractUser
from api.manager import UserManager

from utils.options import IdentificationTypeOptions

class User(AbstractUser):
    """ Custom user model."""
    username = None
    USERNAME_FIELD = 'email'
    full_name = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(unique=True)

    identification_type = models.CharField(max_length=20
    , choices=IdentificationTypeOptions.choices,
    help_text='Select a valid identification type.')
    identification_number = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()