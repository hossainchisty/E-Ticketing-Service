from django.db import models
from .bogi_model import Bogi
from utils.options import ClassOptions

class Seat(models.Model):
    ''' A model representing a seat info. '''
    name = models.CharField(max_length=1)
    bogi = models.ForeignKey(Bogi, on_delete=models.CASCADE)
    types = models.CharField(max_length=10, choices=ClassOptions.choices)