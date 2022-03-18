from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid

class Termine(models.Model):
    bezeichnung = models.CharField(max_length=50, verbose_name='Bezeichnung *')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(verbose_name='Datum *')
    time = models.TimeField(verbose_name='Uhrzeit', blank=True, null=True)
    location = models.CharField(max_length=100, verbose_name='Standort', blank=True, null=True)

    def __str__(self):
        return self.bezeichnung[:30] + '...'

class BlogPost(models.Model):
    titel = models.CharField(max_length=50, verbose_name='Titel *')
    creation = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    inhalt = models.CharField(max_length=2000, verbose_name='Inhalt *')
    bild = models.ImageField(blank=True, default="tennisball.png")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date= models.DateField(verbose_name='Datum *')
    standort = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.titel[:30] + '...'

    def snippet(self):
        return self.inhalt[:75] + '...'

class Galerie(models.Model):
    bild = models.ImageField(verbose_name='Bild *')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    beschreibung = models.CharField(blank=True, max_length=100, verbose_name='Beschreibung', null=True)
    creation = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    date= models.DateField(verbose_name='Datum', blank=True, null=True)

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    standort = models.CharField(blank=True, max_length=50, verbose_name='Standort', null=True)
    