from rest_framework import viewsets, permissions
from rest_framework.response import Response
from thing.models import Category
from thing.serializers import CategorySerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def show_all(self, request):
        categories = Category.objects.all()
        serializer = self.get_serializer(categories, many=True)
        data = serializer.data
        return Response(data)