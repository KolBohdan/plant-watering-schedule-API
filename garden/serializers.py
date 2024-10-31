import datetime

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
            "last_watered_date",
            "is_watered"
        )


class PlantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ("last_watered_date",)


class PlantMarkAsWateredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = (
            "id",
            "name",
            "species",
            "watering_frequency_days",
            "last_watered_date",
            "is_watered"
        )
        read_only_fields = fields

    def update(self, instance, validated_data):
        instance.last_watered_date = datetime.date.today()
        instance.save()

        return instance
