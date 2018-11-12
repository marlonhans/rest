from django.urls import path, include
from . import views

urlpatterns = [
    path('created-by', views.ListViewset.as_view({'get': 'created_by'})),
    path('applied-by', views.ListViewset.as_view({'get': 'applied_by'})),
    path('search', views.ListViewset.as_view({'post': 'search'})),
    path('recommended', views.ListViewset.as_view({'get': 'recommended'})),
]