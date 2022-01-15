from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from animal_crossing_new_horizons.acnh_api.models import Villager


class VillagerSerializer(ModelSerializer):
    class Meta:
        model = Villager
        fields = '__all__'
