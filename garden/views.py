from rest_framework import viewsets, mixins


from garden.models import Plant
from garden.serializers import PlantSerializer


class PlantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
