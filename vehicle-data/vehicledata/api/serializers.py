from rest_framework.serializers import ModelSerializer

from .models import *


class VehicleDataSerializer(ModelSerializer):
    class Meta:
        model = VehicleData
        fields = "__all__"


class VehicleDetailsSerializer(ModelSerializer):
    class Meta:
        model = VehicleData
        fields = "vehicle_type", "vehicle_owner","vehicle_owner_contact"

class ANPREventDataSerializer(ModelSerializer):
    class Meta:
        model = IntoziAiAnprEventData
        fields = "__all__"
