from django.urls import path, include
from .views import *


urlpatterns = [
    path('airline/', AirlineAPIView.as_view()),
    path('airline/<int:pk>', AirlineDetailAPIView.as_view()),
    path('plane/', PlaneAPIView.as_view()),
    path('plane/<int:pk>', PlaneDetailAPIView.as_view()),
    path('flight/', FlightAPIView.as_view()),
    path('flight/<int:pk>', FlightDetailAPIView.as_view()),
]

    