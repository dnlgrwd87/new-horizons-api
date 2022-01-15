from django.db import models


class Villager(models.Model):
    name = models.CharField(max_length=256)
    icon_image = models.CharField(max_length=256)
    house_image = models.CharField(max_length=256)
    species = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    personality = models.CharField(max_length=256)
    birthday = models.CharField(max_length=256)
    catchphrase = models.CharField(max_length=256)
    style1 = models.CharField(max_length=256)
    style2 = models.CharField(max_length=256)
    color1 = models.CharField(max_length=256)
    color2 = models.CharField(max_length=256)
    spreadsheet_id = models.CharField(max_length=256)
