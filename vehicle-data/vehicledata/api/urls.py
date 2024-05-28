from django.urls import path
from .views import *

urlpatterns = [
    # path("vehicledetails/", VehicleDetails.as_view(), name='vehicaldetails'),
    # path("vehiclelist/", VehicleList.as_view(), name='vehicallist'),
    path("vehiclecount/", VehicleCount.as_view(), name='vehicalcount'),
    # path("vehiclecount/", count_vehicle_attributes, name='vehicalcount'),
    path("averagecount/", AverageCount.as_view(), name='averagecount'),
    path("cameracount/", CameraCount.as_view(), name='cameracount'),
]

