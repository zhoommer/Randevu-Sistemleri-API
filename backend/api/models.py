from django.db import models

# Create your models here.

PERSONEL_CHOISES = {
        "EM": "EMRAH",
        "LM": "LOKMAN"
        }


class Randevular(models.Model):
    tarih = models.DateField()
    name_surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    personel = models.CharField(choices=PERSONEL_CHOISES, max_length=2)
    saat = models.CharField(max_length=10)
    note = models.TextField()
    onay_durumu = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Randevular"
        verbose_name_plural = "Randevular"


    def __str__(self):
        return f"{self.name_surname}"


