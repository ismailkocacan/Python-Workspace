from django.db import models


class Kategori(models.Model):
    id = models.AutoField(primary_key=True)
    adi = models.CharField(max_length=20)
    class Meta:
        app_label = 'djangomvctestapp'

class Kisi(models.Model):
    id = models.AutoField(primary_key=True)
    kategori = models.ForeignKey(Kategori)
    adi = models.CharField(max_length=20)
    soyadi = models.CharField(max_length=20)
    yasi = models.IntegerField()
    evli = models.BooleanField()
    class Meta:
        app_label = 'djangomvctestapp'



