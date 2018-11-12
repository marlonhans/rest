from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    #profile = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = '__all__'

    # def get_profile(self, obj):
    #     return Profile.objects.get(user=obj)

