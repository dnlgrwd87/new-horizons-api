from django.test import Client, TestCase
from django.urls import reverse
from django_dynamic_fixture import G

from animal_crossing_new_horizons.acnh_api.models import Villager, Fossil, Fish, Insect


class APITestVillagers(TestCase):
    def test_villagers_api(self):
        G(Villager, name='tom')
        G(Villager, name='jerry')

        c = Client()

        response = c.get(reverse('villagers-list'))

        self.assertEqual(2, len(response.json()['results']))

    def test_villagers_api_filters(self):
        G(Villager, name='villager1', personality='personality1')
        G(Villager, name='villager2', personality='personality2')

        c = Client()

        filters = {
            'personality': 'personality1'
        }
        response = c.get(reverse('villagers-list'), data=filters)
        results = response.json()['results']

        self.assertEqual(1, len(results))
        self.assertEqual('villager1', results[0]['name'])


class APITestFossils(TestCase):
    def test_fossils_api(self):
        G(Fossil, name='fossil1')
        G(Fossil, name='fossil2')

        c = Client()

        response = c.get(reverse('fossils-list'))

        self.assertEqual(2, len(response.json()['results']))

    def test_fossils_api_filters(self):
        G(Fossil, name='fossil1', in_catalog=True)
        G(Fossil, name='fossil2', in_catalog=False)

        c = Client()

        filters = {
            'in_catalog': True
        }
        response = c.get(reverse('fossils-list'), data=filters)
        results = response.json()['results']

        self.assertEqual(1, len(results))
        self.assertEqual('fossil1', results[0]['name'])


class APITestFish(TestCase):
    def test_fish_api(self):
        G(Fish, name='fish1')
        G(Fish, name='fish2')

        c = Client()

        response = c.get(reverse('fish-list'))

        self.assertEqual(2, len(response.json()['results']))

    def test_fish_api_filters(self):
        G(Fish, name='fish1', sell_price=200)
        G(Fish, name='fish2', sell_price=500)

        c = Client()

        filters = {
            'sell_price': '200'
        }
        response = c.get(reverse('fish-list'), data=filters)
        results = response.json()['results']

        self.assertEqual(1, len(results))
        self.assertEqual('fish1', results[0]['name'])


class APITestInsects(TestCase):
    def test_insects_api(self):
        G(Insect, name='insects1')
        G(Insect, name='insects2')

        c = Client()

        response = c.get(reverse('insects-list'))

        self.assertEqual(2, len(response.json()['results']))

    def test_insects_api_filters(self):
        G(Insect, name='insects1', sell_price=200)
        G(Insect, name='insects2', sell_price=500)

        c = Client()

        filters = {
            'sell_price': '200'
        }
        response = c.get(reverse('insects-list'), data=filters)
        results = response.json()['results']

        self.assertEqual(1, len(results))
        self.assertEqual('insects1', results[0]['name'])
