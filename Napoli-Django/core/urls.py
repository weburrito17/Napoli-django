from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('squad/', views.squad, name='squad'),
    path('matches/', views.matches, name='matches'),
    path('stats/', views.stats, name='stats'),
]