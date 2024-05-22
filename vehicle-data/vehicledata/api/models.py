from django.db import models

# Create your models here.
class VehicleData(models.Model):
    vehicle_type = models.CharField(max_length=100)
    vehicle_company = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_plate_number = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=50)
    vehicle_owner = models.CharField(max_length=100)
    vehicle_owner_contact = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_type