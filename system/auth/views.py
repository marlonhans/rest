from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from system.serializers import UserSerializer
from system.models import Profile
import re
from rest_framework import viewsets, status, permissions

@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def try_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    data = serializer.data
    return Response({'token': token.key, 'userAccount': data}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    email = request.data.get('email')
    password = request.data.get('password')
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    phone = request.data.get('phone')
    photo_file = request.data.get('photo_file')

    # lists = request.data.dict()
    # mores = {k.replace('more[', '').replace(']',''):v for k, v in lists.items() if re.match(r'more\[.*?\]',k)}

    if not username or not password or not email or not phone or not first_name or not last_name:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    new_user = User.objects.create_user(username=username, password=password, email=email)
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.save()
    new_profile = Profile(user=new_user, phone=phone)
    if photo_file:
        new_profile.photo = photo_file
    new_profile.save()

    # if mores:
    #     for k,v in mores.items():
    #         userMore = UserMore(user=new_user, key=k, value=v)
    #         userMore.save()
    # token, _ = Token.objects.get_or_create(user=new_user)
    return Response(status=status.HTTP_200_OK)