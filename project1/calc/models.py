from django.db import models

# Create your models here.


class Desination(models.Model):
    name = models.CharField(max_length=100, default='')
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics', default='')
    price = models.IntegerField()
