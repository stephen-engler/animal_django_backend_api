from django.db import models
"""
Contains Model For Animal class
"""

#Animal Class
class Animal(models.Model):
    """
    Model for Animal Class, commonName, scientificName, family, imageURL
    """
    commonName = models.CharField(max_length=100, blank=True, default='')
    scientificName = models.CharField(max_length=100, blank=True, default='')
    family = models.CharField(max_length=100, blank=True, default='')
    imageURL = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('commonName',)
