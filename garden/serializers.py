from rest_framework import serializers

from garden.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = (
            "id",
            "name",
            "species",
            "watering_frequency_days",
            "last_watered_date"
        )
