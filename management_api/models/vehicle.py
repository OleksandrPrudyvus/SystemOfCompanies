from django.db import models


class Vehicle(models.Model):
    """A model that is a representation of the Vehicle table in the database"""

    licence_plate = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year_of_manufacture = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ManyToManyField('User', blank=True, null=True)

    def __str__(self):
        return f'{self.company}-{self.office}-{self.name}-{self.model}'