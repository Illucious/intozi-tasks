import time
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.views.generic import View  
from django.shortcuts import render
from django.http import StreamingHttpResponse
from rest_framework import status
from faker import Faker

from .models import VehicleData
from .serializers import VehicleDataSerializer





# Create your views here.

class StreamGeneratorView(APIView):
    def get(self, request, *args, **kwargs):
        def stream_generator():
            queryset = VehicleData.objects.all()
            serializer = VehicleDataSerializer(queryset, many=True)
            for data in serializer.data:
                yield JSONRenderer().render(data)
                # time.sleep(1)  # Add a delay between each response
                # print("wait")

        # response = StreamingHttpResponse(stream_generator())
        # response['Content-Type'] = 'application/json'
        # response['Cache-Control'] = 'no-cache'
        return StreamingHttpResponse(stream_generator())

        # return response
