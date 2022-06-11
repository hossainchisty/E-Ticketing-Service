from .timestamp_model import Timestamp
from django.db import models

class Station(Timestamp):
    ''' A model representing a station info. '''
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.name