from django.db import models

class Bayer(models.Model): #Модель покупателя
    name = models.CharField(max_length=20)
    balance  = models.DecimalField(decimal_places=2, max_digits=10)
    age = models.IntegerField()

class Game(models.Model): #Модель игр
    title = models.CharField(max_length=20)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    description  = models.TextField()
    age_limited = models.BooleanField(default=True)
    buyer = models.ManyToManyField(Bayer)