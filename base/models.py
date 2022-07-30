from pickle import TRUE
from django.db import models

# Create your models here.

class Branches(models.Model):
    name = models.CharField(max_length=100)
    seats_total = models.CharField(max_length=3)
    seats_remain = models.IntegerField()
    cutoff = models.FloatField(max_length=6)
    
    def __str__(self):
        return self.name
