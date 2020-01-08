from django.db import models


# Create your models here.
class Recipe(models.Model):
    creater = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    process = models.CharField(max_length=200)
    image = models.ImageField(width_field=None, height_field=None)
    date = models.DateField("prepared date")

    def __str__(self):
        return self.name


