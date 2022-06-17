from django.db import models
from .station_model import Station
from .user_model import CustomUser

class Train(models.Model):
    ''' A model representing a train info. '''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    station_form = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_form')
    station_to = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_to')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    train_name = models.CharField(max_length=100)
    train_number = models.CharField(max_length=100)
    journey_time = models.DateTimeField()
    issued_time = models.DateTimeField()
    seat_number = models.CharField(max_length=2)


    class Meta:
        ordering = ['-issued_time']

    def __str__(self):
        return self.train_name
    