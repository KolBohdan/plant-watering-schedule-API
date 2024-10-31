from rest_framework import viewsets, mixins


from garden.models import Plant
from garden.serializers import PlantSerializer, PlantUpdateSerializer


class PlantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Plant.objects.all()


    def get_serializer_class(self):
        if self.action == "update":
            return PlantUpdateSerializer
        return PlantSerializer
