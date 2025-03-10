from django.urls import path
from dotaapp import views


urlpatterns = [
    path('', views.player_matches, name='player_matches'),
]