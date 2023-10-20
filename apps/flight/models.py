from django.db import models
from apps.plane.models import Plane
from apps.airline.models import Airline

class Flight(models.Model):
    from_c = models.CharField(max_length=256)
    to = models.CharField(max_length=256)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.from_c}'

