from rest_framework.routers import DefaultRouter

from animal_crossing_new_horizons.acnh_api.views import VillagerModelViewSet, FossilModelViewSet

router = DefaultRouter()
router.register(r'villagers', VillagerModelViewSet, basename='villagers')
router.register(r'fossils', FossilModelViewSet, basename='fossils')
urlpatterns = router.urls
