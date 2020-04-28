from django.db import models


# Create your models here.
class Movie(models.Model):

    title = models.CharField("Movie Title", max_length=100, null=True, blank=False)
    synopsys = models.CharField("Synospys", max_length=100, null=True, blank=True)
    release_year = models.CharField("Release year", max_length=100, null=True, blank=True)
    duration = models.IntegerField('Duration', blank=True, default=10, null=True)


# Create your models here.
class Actor(models.Model):

    first = models.CharField("First Name", max_length=100, null=True, blank=False)
    last = models.CharField("Last Name", max_length=100, null=True, blank=True)
    birthdate = models.CharField("Birthdate", max_length=100, null=True, blank=True)
