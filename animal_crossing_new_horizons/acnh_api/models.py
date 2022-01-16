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

    @property
    def styles(self):
        return [self.style1, self.style2]

    @property
    def colors(self):
        return [self.color1, self.color2]


class Fossil(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    size = models.CharField(max_length=256)
    source = models.CharField(max_length=256)
    color1 = models.CharField(max_length=256)
    color2 = models.CharField(max_length=256)
    interactive = models.BooleanField()
    can_reorder = models.BooleanField()
    in_catalog = models.BooleanField()
    museum_description = models.CharField(max_length=1000)
    spreadsheet_id = models.CharField(max_length=256)

    @property
    def colors(self):
        return [self.color1, self.color2]
