from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from animal_crossing_new_horizons.acnh_api.models import Villager, Fossil, Insect, Fish


class VillagerSerializer(ModelSerializer):
    class Meta:
        model = Villager
        fields = [
            'id',
            'name',
            'icon_image',
            'house_image',
            'species',
            'gender',
            'personality',
            'birthday',
            'catchphrase',
            'styles',
            'colors',
        ]


class FossilSerializer(ModelSerializer):
    class Meta:
        model = Fossil
        fields = [
            'id',
            'name',
            'image',
            'museum_description',
            'buy_price',
            'sell_price',
            'size',
            'source',
            'interactive',
            'can_reorder',
            'in_catalog',
            'colors',
        ]


class FishSerializer(ModelSerializer):
    class Meta:
        model = Fish
        fields = [
            'id',
            'name',
            'critterpedia_image',
            'icon_image',
            'furniture_image',
            'museum_description',
            'catch_phrase',
            'source',
            'sell_price',
            'colors',
            'lighting_type',
            'shadow',
            'size'
        ]


class InsectSerializer(ModelSerializer):
    class Meta:
        model = Insect
        fields = [
            'id',
            'name',
            'critterpedia_image',
            'icon_image',
            'furniture_image',
            'museum_description',
            'catch_phrase',
            'source',
            'sell_price',
            'colors',
            'weather',
        ]
