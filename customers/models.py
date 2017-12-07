from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, blank=True, null=True, unique=True)
    city = models.ForeignKey('cities.City', null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)