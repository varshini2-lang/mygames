# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('word/', views.wordle, name='home'),  # If you have a home view
    path('connect/', views.connect_four, name='connect_four'),
    path('flappy/', views.flappybird, name='flappy'),
    path('2048/', views.index, name='flappy'),
]
