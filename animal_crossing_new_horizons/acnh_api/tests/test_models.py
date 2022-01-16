from django.test import TestCase
from django_dynamic_fixture import G

from animal_crossing_new_horizons.acnh_api.models import Villager, BaseModel


class BaseModelTest(TestCase):

    def test_base_model_colors_property(self):
        # Use any model that inherits from BaseModel
        villager = G(Villager)

        self.assertTrue(issubclass(Villager, BaseModel))
        self.assertEqual([villager.color1, villager.color2], villager.colors)
