from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.response import Response

from django.contrib.auth import authenticate

from .serializers import *
from .models import *


class VehicleList(generics.ListAPIView):
    queryset = VehicleData.objects.all()
    serializer_class = VehicleDataSerializer
    

class VehicleDetails(APIView):
    # queryset = VehicleData.objects.all()
    # serializer_class = VehicleDetailsSerializer
    def get(self, request, *args, **kwargs):
        vehicle_type_list = VehicleData.objects.values_list('vehicle_type', flat=True).distinct()

        # vehicle_type_list = ["Car", "Bike", "Truck", "Bus"]
        details = {}

        for vehicle_type in vehicle_type_list:
            queryset = VehicleData.objects.filter(vehicle_type=vehicle_type)
            serializer = VehicleDetailsSerializer(queryset, many=True)
            details[vehicle_type] = serializer.data

        return Response(details, status=status.HTTP_200_OK)





    # def get_queryset(self):
    #     vehicle_type_list = ["Car", "Bike", "Truck", "Bus"]
    #     details = {}
    #     for vehicle_type in vehicle_type_list:
    #         if vehicle_type == self.kwargs.get('vehicle_type'):
    #             queryset = VehicleData.objects.filter(vehicle_type=vehicle_type)
    #             serializer = VehicleDetailsSerializer(queryset, many=True)
    #             details[vehicle_type] = serializer.data
    #     return Response(details, status=status.HTTP_200_OK)
                
    #     vehicle_type = self.kwargs.get('vehicle_type')
    #     print(f"Looking up vehicle_type: {vehicle_type}")  # Debugging line
    #     queryset = VehicleData.objects.filter(vehicle_type=vehicle_type)
    #     print(f"Found {queryset.count()} records for vehicle_type: {vehicle_type}")  # Debugging line
    #     return queryset
    # # def get(self, request, *args, **kwargs):
    # #     vehicle_type = kwargs.get('vehicle_type')
    # #     try:
    # #         vehicle = VehicleData.objects.filter(vehicle_type=vehicle_type)
    # #         serializer = VehicleDetailsSerializer(vehicle)
    # #         return Response(serializer.data, status=status.HTTP_200_OK)
    # #     except VehicleData.DoesNotExist:
    # #         return Response({"message": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)

