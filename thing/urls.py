from django.urls import path, include

urlpatterns = [
    path('', include('thing.thing.urls')),
    path('category/', include('thing.category.urls')),
    path('city/', include('thing.city.urls')),
    path('list/', include('thing.list.urls')),
    path('setting/', include('thing.setting.urls')),
    path('social/', include('thing.social.urls')),
]