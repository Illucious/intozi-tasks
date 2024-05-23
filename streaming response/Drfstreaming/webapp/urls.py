from django.urls import path

from . import views

urlpatterns = [
 path('stream/',views.StreamGeneratorView.as_view(),name='generate_stream'),
]