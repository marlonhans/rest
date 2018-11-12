from rest_framework import viewsets, permissions
from rest_framework.response import  Response
from thing.models import PriceType, Type, Category, City
from thing.serializers import PriceTypeSerializer, TypeSerializer, CategorySerializer, CitySerializer

class PriceTypeViewset(viewsets.ModelViewSet):
    queryset = PriceType.objects.all()
    serializer_class = PriceTypeSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        priceTypes = PriceType.objects.all()
        serializer = self.get_serializer(priceTypes, many=True)
        data = serializer.data
        return Response(data)

class TypeViewset(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        types = Type.objects.all()
        serializer = self.get_serializer(types, many=True)
        data = serializer.data
        return Response(data)

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        categories = Category.objects.all()
        serializer = self.get_serializer(categories, many=True)
        data = serializer.data
        return Response(data)

class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        cities = City.objects.all()
        serializer = self.get_serializer(cities, many=True)
        data = serializer.data
        return Response(data)