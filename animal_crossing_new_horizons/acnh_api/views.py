from rest_framework.viewsets import ReadOnlyModelViewSet

from animal_crossing_new_horizons.acnh_api.models import Villager, Fossil, Fish, Insect
from animal_crossing_new_horizons.acnh_api.serializers import VillagerSerializer, FossilSerializer, FishSerializer, \
    InsectSerializer


class VillagerModelViewSet(ReadOnlyModelViewSet):
    queryset = Villager.objects.order_by('id').all()
    serializer_class = VillagerSerializer

    filter_fields = ('gender', 'personality')


class FossilModelViewSet(ReadOnlyModelViewSet):
    queryset = Fossil.objects.order_by('id').all()
    serializer_class = FossilSerializer

    filter_fields = ('in_catalog',)


class FishModelViewSet(ReadOnlyModelViewSet):
    queryset = Fish.objects.order_by('id').all()
    serializer_class = FishSerializer

    filter_fields = ('sell_price',)


class InsectModelViewSet(ReadOnlyModelViewSet):
    queryset = Insect.objects.order_by('id').all()
    serializer_class = InsectSerializer

    filter_fields = ('sell_price',)
