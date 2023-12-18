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
def get_nfl_players(request):
    players = NFLPlayers.objects.all()
    serializer = NFLPlayersSerializer(players, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_nfl_player(request, pk):
    players = NFLPlayers.objects.get(player_id=pk)
    serializer = NFLPlayersSerializer(players, many=False)
    return Response(serializer.data)