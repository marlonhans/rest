from django.urls import path
from . import views

urlpatterns = [
    path('all', views.CategoryViewset.as_view({'get': 'show_all'})),
]