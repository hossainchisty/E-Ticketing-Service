from .timestamp import Timestamp
from django.db import models
from .station_model import Station
from .user_model import CustomUser

class Ticket(Timestamp):
    ''' A model representing a ticket info. '''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    station_form = models.ForeignKey(Station, on_delete=models.CASCADE)
    station_to = models.ForeignKey(Station, on_delete=models.CASCADE)
    price = models.IntegerField()
    train_name = models.CharField(max_length=100)
    train_number = models.CharField(max_length=100)
    journey_datetime = models.DateTimeField()
    issued_datetime = models.DateTimeField()
