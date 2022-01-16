from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from animal_crossing_new_horizons.acnh_api.models import Villager, Fossil


class VillagerSerializer(ModelSerializer):
    class Meta:
        model = Villager
        fields = [
            'name',
            'icon_image',
            'house_image',
            'species',
            'gender',
            'personality',
            'birthday',
            'catchphrase',
            'styles',
            'colors'
        ]


class FossilSerializer(ModelSerializer):
    class Meta:
        model = Fossil
        fields = [
            'name',
            'museum_description',
            'image',
            'buy_price',
            'sell_price',
            'size',
            'source',
            'interactive',
            'can_reorder',
            'in_catalog',
            'colors',
        ]
