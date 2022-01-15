from rest_framework.routers import DefaultRouter

from animal_crossing_new_horizons.acnh_api.views import VillagerModelViewSet

router = DefaultRouter()
router.register(r'villagers', VillagerModelViewSet, basename='villagers')
urlpatterns = router.urls
