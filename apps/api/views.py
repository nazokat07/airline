from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from apps.airline.models import Airline
from apps.flight.models import Flight
from apps.plane.models import Plane

from .serializers import FlightSerializer
from .serializers import AirlineSerializer
from .serializers import PlaneSerializer



class FlightAPIView(APIView):

    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = FlightSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class FlightDetailAPIView(APIView):

    def get(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializer(Flight)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializer(Flight, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        flight.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    









class AirlineAPIView(APIView):

    def get(self, request):
        airline = Airline.objects.all()
        serializer = AirlineSerializer(airline, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = AirlineSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class AirlineDetailAPIView(APIView):

    def get(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        serializer = AirlineSerializer(Airline)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        serializer = AirlineSerializer(Airline, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        airline.delete()
        return Response(status=HTTP_204_NO_CONTENT)






class PlaneAPIView(APIView):

    def get(self, request):
        plane = Plane.objects.all()
        serializer = PlaneSerializer(plane, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = PlaneSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class PlaneDetailAPIView(APIView):

    def get(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializer = PlaneSerializer(Flight)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializer = PlaneSerializer(Flight, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        plane.delete()
        return Response(status=HTTP_204_NO_CONTENT)


    
