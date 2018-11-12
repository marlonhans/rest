from rest_framework import viewsets, permissions
from rest_framework.response import Response
from thing.models import City
from thing.serializers import CitySerializer

class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]

    def show_all(self, request):
        cities = City.objects.all()
        serializer = self.get_serializer(cities, many=True)
        data = serializer.data
        return Response(data)