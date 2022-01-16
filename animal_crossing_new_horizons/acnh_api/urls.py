from rest_framework.routers import DefaultRouter

from animal_crossing_new_horizons.acnh_api.views import VillagerModelViewSet, FossilModelViewSet, FishModelViewSet, \
    InsectModelViewSet

router = DefaultRouter()
router.register(r'villagers', VillagerModelViewSet, basename='villagers')
router.register(r'fossils', FossilModelViewSet, basename='fossils')
router.register(r'fish', FishModelViewSet, basename='fish')
router.register(r'insects', InsectModelViewSet, basename='insects')
urlpatterns = router.urls
