import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from garden.models import Plant

PLANT_URL = reverse("garden:plant-list")


def detail_url(plant_id: int):
    return reverse("garden:plant-detail", args=[plant_id])


def mark_as_watered_url(plant_id: int):
    return reverse("garden:plant-mark-as-watered", args=[plant_id])


def sample_plant(**params) -> Plant:
    defaults = {
        "name": "rose",
        "species": "flower",
        "watering_frequency_days": 5,
        "last_watered_date": datetime.date(2024, 10, 5),
    }
    defaults.update(params)

    return Plant.objects.create(**defaults)


class UpdateLastWateredDateTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_update_last_watered_date(self):
        plant = sample_plant()
        plant_url = detail_url(plant.id)

        date = datetime.date(2024, 10, 20)

        payload = {
            "last_watered_date": date,
        }

        res = self.client.put(plant_url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_mark_as_watered(self):
        plant = sample_plant()

        self.client.put(mark_as_watered_url(plant.id))

        instance = Plant.objects.get(pk=plant.id)
        current_date = datetime.date.today()

        self.assertEqual(instance.last_watered_date, current_date)
