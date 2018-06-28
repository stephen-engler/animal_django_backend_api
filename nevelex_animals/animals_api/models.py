from django.db import models

# Create your models here.

class Animal(models.Model):
    commonName = models.CharField(max_length=100, blank=True, default='')
    scientificName = models.CharField(max_length=100, blank=True, default='')
    family = models.CharField(max_length=100, blank=True, default='')
    imageURL = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('commonName',)
