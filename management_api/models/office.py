from django.db import models
from django.urls import reverse


class Office(models.Model):
    """A model that is a representation of the Office table in the database"""

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('retrieve_office', kwargs={'id': self.pk})

    def __str__(self):
        return f'{self.company}-{self.name}-{self.country}-{self.city}'