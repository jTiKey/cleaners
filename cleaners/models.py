from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Cleaner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    quality_score = models.DecimalField(max_digits=5, decimal_places=2,
                                        validators=[MaxValueValidator(5), MinValueValidator(0)])
    cities = models.ManyToManyField('cities.City')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)