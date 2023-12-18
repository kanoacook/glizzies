from django.urls import path
from ..views import player_views as views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('', views.get_nfl_players, name='nfl-players'),
    path('<str:pk>', views.get_nfl_player, name='nfl-player'),

    # path('profile/update/', views.updateUserProfile, name='user-profile-update'),
    # path('', views.getUsers, name='users'),

]