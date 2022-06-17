from django.db import models
from .train_model import Train
class Bogi(models.Model):
    ''' A model representing a Bogi info. '''
    name = models.CharField(max_length=10)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)

    def __str__(self):
        return self.name