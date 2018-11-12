from django.urls import path, include
from . import views

urlpatterns = [
    path('price-type', views.PriceTypeViewset.as_view({'get': 'list'})),
    path('type', views.TypeViewset.as_view({'get': 'list'})),
    path('category', views.CategoryViewset.as_view({'get': 'list'})),
    path('city', views.CityViewset.as_view({'get': 'list'})),
]