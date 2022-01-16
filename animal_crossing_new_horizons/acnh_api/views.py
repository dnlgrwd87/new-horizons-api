from rest_framework.viewsets import ReadOnlyModelViewSet

from animal_crossing_new_horizons.acnh_api.models import Villager, Fossil, Fish, Insect
from animal_crossing_new_horizons.acnh_api.serializers import VillagerSerializer, FossilSerializer, FishSerializer, \
    InsectSerializer


class VillagerModelViewSet(ReadOnlyModelViewSet):
    queryset = Villager.objects.all()
    serializer_class = VillagerSerializer

    filter_fields = ('species',)


class FossilModelViewSet(ReadOnlyModelViewSet):
    queryset = Fossil.objects.all()
    serializer_class = FossilSerializer


class FishModelViewSet(ReadOnlyModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer


class InsectModelViewSet(ReadOnlyModelViewSet):
    queryset = Insect.objects.all()
    serializer_class = InsectSerializer
