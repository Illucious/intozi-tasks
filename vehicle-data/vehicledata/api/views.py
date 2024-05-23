from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.db import connection
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.db.models import F, Value, CharField, JSONField, Func, Aggregate, ExpressionWrapper
from django.db.models.functions import Concat, 

from collections import defaultdict
from itertools import groupby
from operator import itemgetter
import json


from .serializers import *
from .models import *


class VehicleList(generics.ListAPIView):
    queryset = VehicleData.objects.all()
    serializer_class = VehicleDataSerializer
    

# class VehicleDetails(APIView):
#     def get(self, request, *args, **kwargs):
#         # Retrieve and serialize data
#         queryset = VehicleData.objects.all().order_by('vehicle_type')
#         serializer = VehicleDetailsSerializer(queryset, many=True)
#         sorted_data = serializer.data
#         pprint(sorted_data)

#         # Use defaultdict to automatically handle missing keys
#         grouped_data = defaultdict(list)
#         # print(grouped_data)
#         for item in sorted_data:
#             grouped_data[item['vehicle_type']].append(item)

#         # Convert defaultdict back to a regular dict
#         grouped_data = dict(grouped_data)

#         return Response(grouped_data, status=status.HTTP_200_OK)

# class VehicleDetails(APIView):
#     def get(self, request, *args, **kwargs):
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT vehicle_type,
#                        json_agg(json_build_object(
#                            'vehicle_owner', vehicle_owner,
#                            'vehicle_owner_contact', vehicle_owner_contact
#                        )) AS details
#                 FROM api_vehicledata
#                 GROUP BY vehicle_type
#                 ORDER BY vehicle_type;
#             """)
#             result = cursor.fetchall()

#         # Constructing the response dictionary
#         grouped_data = {row[0]: row[1] for row in result}

#         return Response(grouped_data, status=status.HTTP_200_OK)


# class JSONAgg(Aggregate):
#     function = 'json_agg'

class VehicleDetails(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve and serialize data
        queryset = VehicleData.objects.annotate(
            vehicle_details=Func(
                Concat(
                    Value('{"vehicle_owner": '), F('vehicle_owner'), 
                    Value(', "vehicle_owner_contact": '), F('vehicle_owner_contact'), 
                    output_field=JSONField()
                ),
                function='json_build_object',
                output_field=JSONField()
            )
        ).values('vehicle_type').annotate(details=JSONAgg('vehicle_details')).order_by('vehicle_type')

        serializer = VehicleDetailsSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

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

