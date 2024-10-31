import datetime

from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from garden.models import Plant
from garden.serializers import (
    PlantSerializer,
    PlantUpdateSerializer,
    PlantMarkAsWateredSerializer,
)


class PlantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Plant.objects.all()

    def get_serializer_class(self):
        if self.action == "update":
            return PlantUpdateSerializer
        elif self.action == "mark_as_watered":
            return PlantMarkAsWateredSerializer

        return PlantSerializer

    @action(
        methods=["PUT"],
        detail=True,
        url_path="mark",
    )
    def mark_as_watered(self, request, pk=None):
        """Endpoint for marking specific plant as watered"""
        plant = self.get_object()
        serializer = self.get_serializer(plant, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
