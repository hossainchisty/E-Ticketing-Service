from django.db import models
from .train_model import Train
from .station_model import Station

class Schedule(models.Model):
    ''' A model representing a Schedule info. '''
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    time = models.TimeField()
    ac_b_price = models.DecimalField(max_digits=4, decimal_places=2)
    ac_s_price = models.DecimalField(max_digits=4, decimal_places=2)
    snigdha_price = models.DecimalField(max_digits=4, decimal_places=2)
    f_berth_price = models.DecimalField(max_digits=4, decimal_places=2)
    f_seat_price = models.DecimalField(max_digits=4, decimal_places=2)
    s_chair_price = models.DecimalField(max_digits=4, decimal_places=2)
    shovan_price = models.DecimalField(max_digits=4, decimal_places=2)