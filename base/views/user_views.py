from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.db import IntegrityError

from django.contrib.auth.hashers import make_password
from rest_framework import status

from ..models import *
from ..serializers import *




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k] = v
        return data
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create_user(
            username=data['email'],  # Assuming email is used as username
            email=data['email'],
            password=data['password'],
        )
        # Use create_user to handle password hashing
        profile = UserProfile.objects.create(
            user=user,
            sleeper_id=data['sleeper_id'],
            sleeper_team_name=data['sleeper_team_name'],
            sleeper_display_name=data['sleeper_display_name'],
            sleeper_league_id=data['sleeper_league_id'],
            email=data['email'],
            sleeper_avatar=data['sleeper_avatar']
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except IntegrityError as e:
        message = {'detail': 'Error: User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        message = {'detail': 'Error occurred: ' + str(e)}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
