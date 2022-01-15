from rest_framework.viewsets import ReadOnlyModelViewSet

from animal_crossing_new_horizons.acnh_api.models import Villager
from animal_crossing_new_horizons.acnh_api.serializers import VillagerSerializer


class VillagerModelViewSet(ReadOnlyModelViewSet):
    queryset = Villager.objects.all()
    serializer_class = VillagerSerializer

    filter_fields = ('species',)
