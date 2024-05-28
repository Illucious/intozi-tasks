from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# for counting timely averages
from django.db.models.functions import TruncHour, TruncDay, TruncWeek, TruncMonth, TruncYear

from django.db.models import Count, Avg
from .serializers import *
from .models import *


# class VehicleList(generics.ListAPIView):
#     queryset = VehicleData.objects.all()
#     serializer_class = VehicleDataSerializer
    

# class VehicleDetails(APIView):
#     def get(self, request, *args, **kwargs):
#         # Retrieve and serialize data
#         queryset = VehicleData.objects.all().order_by('vehicle_class')
#         serializer = VehicleDetailsSerializer(queryset, many=True)
#         sorted_data = serializer.data
#         pprint(sorted_data)

#         # Use defaultdict to automatically handle missing keys
#         grouped_data = defaultdict(list)
#         # print(grouped_data)
#         for item in sorted_data:
#             grouped_data[item['vehicle_class']].append(item)

#         # Convert defaultdict back to a regular dict
#         grouped_data = dict(grouped_data)

#         return Response(grouped_data, status=status.HTTP_200_OK)

# class VehicleDetails(APIView):
#     def get(self, request, *args, **kwargs):
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT vehicle_class,
#                        json_agg(json_build_object(
#                            'vehicle_owner', vehicle_owner,
#                            'vehicle_owner_contact', vehicle_owner_contact
#                        )) AS details
#                 FROM api_vehicledata
#                 GROUP BY vehicle_class
#                 ORDER BY vehicle_class;
#             """)
#             result = cursor.fetchall()

#         # Constructing the response dictionary
#         grouped_data = {row[0]: row[1] for row in result}

#         return Response(grouped_data, status=status.HTTP_200_OK)


# class JSONAgg(Aggregate):
#     function = 'json_agg'

# class VehicleDetails(APIView):
#     def get(self, request, *args, **kwargs):
#         # Retrieve and serialize data
#         queryset = VehicleData.objects.annotate(
#             vehicle_details=Func(
#                 Concat(
#                     Value('{"vehicle_owner": '), F('vehicle_owner'), 
#                     Value(', "vehicle_owner_contact": '), F('vehicle_owner_contact'), 
#                     output_field=JSONField()
#                 ),
#                 function='json_build_object',
#                 output_field=JSONField()
#             )
#         ).values('vehicle_class').annotate(details=JSONAgg('vehicle_details')).order_by('vehicle_class')

#         serializer = VehicleDetailsSerializer(queryset, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     vehicle_class_list = ["Car", "Bike", "Truck", "Bus"]
    #     details = {}
    #     for vehicle_class in vehicle_class_list:
    #         if vehicle_class == self.kwargs.get('vehicle_class'):
    #             queryset = VehicleData.objects.filter(vehicle_class=vehicle_class)
    #             serializer = VehicleDetailsSerializer(queryset, many=True)
    #             details[vehicle_class] = serializer.data
    #     return Response(details, status=status.HTTP_200_OK)
                
    #     vehicle_class = self.kwargs.get('vehicle_class')
    #     print(f"Looking up vehicle_class: {vehicle_class}")  # Debugging line
    #     queryset = VehicleData.objects.filter(vehicle_class=vehicle_class)
    #     print(f"Found {queryset.count()} records for vehicle_class: {vehicle_class}")  # Debugging line
    #     return queryset
    # # def get(self, request, *args, **kwargs):
    # #     vehicle_class = kwargs.get('vehicle_class')
    # #     try:
    # #         vehicle = VehicleData.objects.filter(vehicle_class=vehicle_class)
    # #         serializer = VehicleDetailsSerializer(vehicle)
    # #         return Response(serializer.data, status=status.HTTP_200_OK)
    # #     except VehicleData.DoesNotExist:
    # #         return Response({"message": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)


# class VehicleCount(APIView):
#     def get(self, request, *args, **kwargs):
#         # Extract vehicle_class and vehicle_number from query parameters
#         vehicle_classes = request.query_params.getlist('vehicle_class')
#         vehicle_numbers = request.query_params.getlist('vehicle_number')
        
#         # Debug: Print the vehicle classes and numbers received
#         print(f"Received vehicle_classes: {vehicle_classes}")
#         print(f"Received vehicle_numbers: {vehicle_numbers}")
        
#         # Query the database for counts of each vehicle class
#         class_counts = IntoziAiAnprEventData.objects.filter(
#             vehicle_class__in=vehicle_classes
#         ).annotate(
#             class_count=Count('vehicle_class')
#         ).values(
#             'vehicle_class', 'class_count'
#         )
        
#         # Query the database for counts of each vehicle number
#         number_counts = IntoziAiAnprEventData.objects.filter(
#             vehicle_number__in=vehicle_numbers
#         ).annotate(
#             number_count=Count('vehicle_number')
#         ).values(
#             'vehicle_number', 'number_count'
#         )
        
#         # Create dictionaries for the response
#         class_response_data = {item['vehicle_class']: item['class_count'] for item in class_counts}
#         number_response_data = {item['vehicle_number']: item['number_count'] for item in number_counts}
        
#         # Include vehicle classes and numbers with zero counts in the response
#         class_response_data.update({vc: 0 for vc in vehicle_classes if vc not in class_response_data})
#         number_response_data.update({vn: 0 for vn in vehicle_numbers if vn not in number_response_data})

#         # Combine both dictionaries into a single response
#         response_data = {
#             'vehicle_class_counts': class_response_data,
#             'vehicle_number_counts': number_response_data
#         }

#         return Response(response_data, status=status.HTTP_200_OK)

# # """latest code"""
# from django.http import JsonResponse
# from django.db import connection

# def count_vehicle_attributes(request):
#     # Get query parameters
#     vehicle_classes = request.GET.getlist('vehicle_class')
#     triple_riding = request.GET.get('triple_riding')
#     no_helmet = request.GET.get('no_helmet')
#     no_seatbelt = request.GET.get('no_seatbelt')

#     # Prepare the SQL query
#     query = """
#         SELECT
#             SUM(CASE WHEN vehicle_class = %s THEN 1 ELSE 0 END) AS vehicle_class_count,
#             SUM(CASE WHEN triple_riding = %s THEN 1 ELSE 0 END) AS triple_riding_count,
#             SUM(CASE WHEN no_helmet = %s THEN 1 ELSE 0 END) AS no_helmet_count,
#             SUM(CASE WHEN no_seatbelt = %s THEN 1 ELSE 0 END) AS no_seatbelt_count
#         FROM
#             your_table_name
#     """

#     # Execute the SQL query
#     with connection.cursor() as cursor:
#         cursor.execute(query, [vc for vc in vehicle_classes] + [triple_riding, no_helmet, no_seatbelt])
#         row = cursor.fetchone()

#     # Construct the response
#     response = {
#         'vehicle_class_count': row[0],
#         'triple_riding_count': row[1],
#         'no_helmet_count': row[2],
#         'no_seatbelt_count': row[3]
#     }

#     return JsonResponse(response)


class VehicleCount(APIView):
    """
    API endpoint for counting vehicle_class, vehicle_number, and offesces like triple_riding, no_helmet, no_seatbelt. it will also give the nuber of entries per camera by cam_id.
    url will take query parameters vehicle_class, vehicle_number, triple_riding, no_helmet, no_seatbelt

    example_url: /api/vehiclecount/?vehicle_class=Car&vehicle_class=Bike&vehicle_number=1234&vehicle_number=5678&triple_riding=True&no_helmet=False&no_seatbelt=True

    """

    def get(self, request, *args, **kwargs):
        # Extract vehicle_class and vehicle_number from query parameters
        vehicle_classes = request.query_params.getlist('vehicle_class')
        vehicle_numbers = request.query_params.getlist('vehicle_number')
        triple_riding = request.query_params.get('triple_riding')
        no_helmet = request.query_params.get('no_helmet')
        no_seatbelt = request.query_params.get('no_seatbelt')
        
        # Debug: Print the vehicle classes and numbers received
        print(f"Received vehicle_classes: {vehicle_classes}")
        print(f"Received vehicle_numbers: {vehicle_numbers}")
        print(f"Received triple_riding: {triple_riding}")
        print(f"Received no_helmet: {no_helmet}")
        print(f"Received no_seatbelt: {no_seatbelt}")
        
        # Query the database for counts of each vehicle class
        class_counts = IntoziAiAnprEventData.objects.filter(
            vehicle_class__in=vehicle_classes
        ).values('vehicle_class').annotate(
            class_count=Count('vehicle_class')
        )
        
        # Query the database for counts of each vehicle number
        number_counts = IntoziAiAnprEventData.objects.exclude(
            vehicle_number=None
        ).filter(
            vehicle_number__in=vehicle_numbers
        ).values('vehicle_number').annotate(
            number_count=Count('vehicle_number')
        )

        # Query the database for true values of triple_riding
        triple_riding_counts = IntoziAiAnprEventData.objects.filter(
            triple_riding=triple_riding
        ).values('triple_riding').annotate(
            triple_riding_count=Count('triple_riding')
        )

        # Query the database for true values of no_helmet
        no_helmet_counts = IntoziAiAnprEventData.objects.filter(
            no_helmet=no_helmet
        ).values('no_helmet').annotate(
            no_helmet_count=Count('no_helmet')
        )

        # Query the database for true values of no_seatbelt
        no_seatbelt_counts = IntoziAiAnprEventData.objects.filter(
            no_seatbelt=no_seatbelt
        ).values('no_seatbelt').annotate(
            no_seatbelt_count=Count('no_seatbelt')
        )
        
        # Query the database for counts of each unique cam_id
        cam_counts = IntoziAiAnprEventData.objects.values('cam_id').annotate(
            cam_count=Count('cam_id')
        )

        # Create dictionaries for the response
        class_response_data = {item['vehicle_class']: item['class_count'] for item in class_counts}
        number_response_data = {item['vehicle_number']: item['number_count'] for item in number_counts}
        triple_riding_response_data = {item['triple_riding']: item['triple_riding_count'] for item in triple_riding_counts}
        no_helmet_response_data = {item['no_helmet']: item['no_helmet_count'] for item in no_helmet_counts}
        no_seatbelt_response_data = {item['no_seatbelt']: item['no_seatbelt_count'] for item in no_seatbelt_counts}
        cam_response_data = {item['cam_id']: item['cam_count'] for item in cam_counts}
        cam_response_data.update({cam_id: 0 for cam_id in IntoziAiAnprEventData.objects.values_list('cam_id', flat=True).distinct() if cam_id not in cam_response_data})

        # Include vehicle classes and numbers with zero counts in the response
        class_response_data.update({vc: 0 for vc in vehicle_classes if vc not in class_response_data})
        number_response_data.update({vn: 0 for vn in vehicle_numbers if vn not in number_response_data})

        # Combine both dictionaries into a single response
        response_data = {
            'vehicle_class_counts': class_response_data,
            'vehicle_number_counts': number_response_data,
            'triple_riding_counts': triple_riding_response_data,
            'no_helmet_counts': no_helmet_response_data,
            'no_seatbelt_counts': no_seatbelt_response_data,
            'cam_counts': cam_response_data
        }

        return Response(response_data, status=status.HTTP_200_OK)


class AverageCount(APIView):
    """
    API endpoint for counting average vehicle entries per hour, day, week, month, and year.
    url: /api/averagecount/

    sample response:
    {
        "total_count": 568732,
        "hourly_average": 901,
        "daily_average": 9173,
        "weekly_average": 28436,
        "monthly_average": 71091,
        "yearly_average": 284366
    }
    """

    def get(self, request, *args, **kwargs):
        queryset = IntoziAiAnprEventData.objects.all()
        total_count = queryset.count()

        #daily average
        hourly_average = queryset.annotate(hour=TruncHour('created_datetime')).values('hour').annotate(hour_count=Count('id')).values('hour', 'hour_count').order_by('hour').aggregate(hour_count_avg=Avg('hour_count'))
        hourly_average = int(hourly_average['hour_count_avg'])

        daily_average = queryset.annotate(day=TruncDay('created_datetime')).values('day').annotate(day_count=Count('id')).values('day', 'day_count').order_by('day').aggregate(day_count_avg=Avg('day_count'))
        daily_average = int(daily_average['day_count_avg'])

        weekly_average = queryset.annotate(week=TruncWeek('created_datetime')).values('week').annotate(week_count=Count('id')).values('week', 'week_count').order_by('week').aggregate(week_count_avg=Avg('week_count'))
        weekly_average = int(weekly_average['week_count_avg'])

        monthly_average = queryset.annotate(month=TruncMonth('created_datetime')).values('month').annotate(month_count=Count('id')).values('month', 'month_count').order_by('month').aggregate(month_count_avg=Avg('month_count'))
        monthly_average = int(monthly_average['month_count_avg'])

        yearly_average = queryset.annotate(year=TruncYear('created_datetime')).values('year').annotate(year_count=Count('id')).values('year', 'year_count').order_by('year').aggregate(year_count_avg=Avg('year_count'))
        yearly_average = int(yearly_average['year_count_avg'])

        # print(hourly_average)
        # print(daily_average)



        return Response({
            'total_count': total_count,
            'hourly_average': hourly_average,
            'daily_average': daily_average,
            'weekly_average': weekly_average,
            'monthly_average': monthly_average,
            'yearly_average': yearly_average
        }, status=status.HTTP_200_OK)


class CameraCount(APIView):
    """
    API endpoint for counting average vehicle entries per hour, day, week, month, and year for each camera(cam_id).
    url: /api/cameracount/

    sample response:
    {
        "1": {
            "cam_hourly_average": 532,
            "cam_daily_average": 2875,
            "cam_weekly_average": 4792,
            "cam_monthly_average": 7188,
            "cam_yearly_average": 14376,
            "cam_entries": 14376
        },
        "50": {
            "cam_hourly_average": 316,
            "cam_daily_average": 2533,
            "cam_weekly_average": 2533,
            "cam_monthly_average": 2533,
            "cam_yearly_average": 2533,
            "cam_entries": 2533
        },
        ....
    }
    """
    def get(self, request, *args, **kwargs):
        queryset = IntoziAiAnprEventData.objects.all()

        # Aggregate counts per time period
        hourly_data = queryset.annotate(hour=TruncHour('created_datetime')).values('cam_id', 'hour').annotate(cam_count=Count('id')).order_by('cam_id', 'hour')
        daily_data = queryset.annotate(day=TruncDay('created_datetime')).values('cam_id', 'day').annotate(cam_count=Count('id')).order_by('cam_id', 'day')
        weekly_data = queryset.annotate(week=TruncWeek('created_datetime')).values('cam_id', 'week').annotate(cam_count=Count('id')).order_by('cam_id', 'week')
        monthly_data = queryset.annotate(month=TruncMonth('created_datetime')).values('cam_id', 'month').annotate(cam_count=Count('id')).order_by('cam_id', 'month')
        yearly_data = queryset.annotate(year=TruncYear('created_datetime')).values('cam_id', 'year').annotate(cam_count=Count('id')).order_by('cam_id', 'year')

        # Count total entries per camera
        cam_entries = queryset.values('cam_id').annotate(cam_count=Count('cam_id'))

        # Create a dictionary with cam_id as keys
        response = {
            entry['cam_id']: {
                'cam_hourly_average': 0,
                'cam_daily_average': 0,
                'cam_weekly_average': 0,
                'cam_monthly_average': 0,
                'cam_yearly_average': 0,
                'cam_entries': entry['cam_count']
            }
            for entry in cam_entries
        }

        # Helper function to calculate averages
        def calculate_averages(data, average_key):
            counts = {}
            for item in data:
                cam_id = item['cam_id']
                if cam_id not in counts:
                    counts[cam_id] = []
                counts[cam_id].append(item['cam_count'])
            for cam_id, count_list in counts.items():
                if count_list:  # Ensure there is at least one count to avoid division by zero
                    response[cam_id][average_key] = sum(count_list) // len(count_list)

        # Calculate and set averages
        calculate_averages(hourly_data, 'cam_hourly_average')
        calculate_averages(daily_data, 'cam_daily_average')
        calculate_averages(weekly_data, 'cam_weekly_average')
        calculate_averages(monthly_data, 'cam_monthly_average')
        calculate_averages(yearly_data, 'cam_yearly_average')

        return Response(response, status=status.HTTP_200_OK)
