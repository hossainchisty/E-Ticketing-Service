from .timestamp import Timestamp
from django.db import models

class Station(Timestamp):
    ''' A model representing a station info. '''
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


    class Meta:
        ''' Meta class for Station model. '''
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'


    def __str__(self):
        return self.name