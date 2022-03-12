from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid

class Termine(models.Model):
    bezeichnung = models.CharField(max_length=50, verbose_name='Bezeichnung')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(verbose_name='Datum')
    time = models.TimeField(verbose_name='Uhrzeit')
    location = models.CharField(max_length=100, verbose_name='Standort')

    def __str__(self):
        return self.bezeichnung[:30] + '...'
        