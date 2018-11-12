from django.urls import path, include
from . import views

urlpatterns = [
    path('contact', views.ContactViewset.as_view({'post': 'post'})),
    path('comment', views.CommentViewset.as_view({'post': 'post'})),
    path('visit-thing/<int:thing_id>', views.StatViewset.as_view({'post': 'incVisit', 'get': 'getVisit'}))
]