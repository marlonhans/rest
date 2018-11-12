from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.ThingViewset.as_view({'get': 'get'})),
    path('', views.ThingViewset.as_view({'post': 'post'})),
]