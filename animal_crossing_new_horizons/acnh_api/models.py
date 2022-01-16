from django.db import models


class BaseModel(models.Model):
    spreadsheet_id = models.CharField(max_length=256, unique=True)
    color1 = models.CharField(max_length=256)
    color2 = models.CharField(max_length=256)

    class Meta:
        abstract = True

    @property
    def colors(self):
        return [self.color1, self.color2]


class BaseCritter(BaseModel):
    name = models.CharField(max_length=256)
    critterpedia_image = models.CharField(max_length=256)
    icon_image = models.CharField(max_length=256)
    furniture_image = models.CharField(max_length=256)
    museum_description = models.CharField(max_length=1000)
    catch_phrase = models.CharField(max_length=1000)
    source = models.CharField(max_length=1000)
    sell_price = models.IntegerField()

    class Meta:
        abstract = True


class Villager(BaseModel):
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

    @property
    def styles(self):
        return [self.style1, self.style2]


class Fossil(BaseModel):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    museum_description = models.CharField(max_length=1000)
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    size = models.CharField(max_length=256)
    source = models.CharField(max_length=256)
    interactive = models.BooleanField()
    can_reorder = models.BooleanField()
    in_catalog = models.BooleanField()


class Fish(BaseCritter):
    lighting_type = models.CharField(max_length=256)
    shadow = models.CharField(max_length=256)
    size = models.CharField(max_length=256)


class Insect(BaseCritter):
    weather = models.CharField(max_length=256)
