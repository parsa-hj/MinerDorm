from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Dorm(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    review = models.TextField(null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name