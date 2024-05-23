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

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     # Convert the data to a list of tuples
    #     data_list = list(data.items())
    #     # Slice the list to include only the third to the last item
    #     third_to_last_data = dict(data_list[2:])
    #     return third_to_last_data
    