from django.db import models


class Company(models.Model):
    """A model that is a representation of the Company table in the database"""
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'