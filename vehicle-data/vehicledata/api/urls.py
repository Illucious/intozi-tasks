from django.urls import path
from .views import *

urlpatterns = [
    path("vehicledetails/", VehicleDetails.as_view(), name = 'vehicaldetails'),
    path("vehiclelist/", VehicleList.as_view(), name = 'vehicallist'),
]

