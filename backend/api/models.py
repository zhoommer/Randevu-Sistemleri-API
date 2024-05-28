import random
import string
from django.db import models


# Create your models here.

PERSONEL_CHOISES = {
        "EMRAH": "EMRAH",
        "LOKMAN": "LOKMAN"
        }




class Personeller(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Personeller"
        verbose_name_plural = "Personeller"

    def __str__(self):
        return f"{self.name} - {self.surname}"



class Randevular(models.Model):
    personel = models.ForeignKey(Personeller, on_delete=models.CASCADE) 
    date = models.DateField()
    name_surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    hour = models.CharField(max_length=10)
    islem = models.JSONField(default=list)
    note = models.TextField(blank=True, null=True)
    onay_durumu = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Randevular"
        verbose_name_plural = "Randevular"


    def __str__(self):
        return f"{self.name_surname}"

    

    

