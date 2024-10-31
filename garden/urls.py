from django.urls import path, include
from rest_framework import routers

from garden.views import PlantViewSet

router = routers.DefaultRouter()


router.register("", PlantViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "garden"
