from django.urls import path
from myapp.views import connect_four
from myapp.views import wordle
from myapp.views import home
from myapp.views import flappybird
from myapp.views import index
urlpatterns = [
    path('',home ,name='home'),
    path('connect_four.html/', connect_four, name='home'),
    path('wordle.html/', wordle, name='home'),
    path('flappybird.html/', flappybird, name='home'),
    path('index.html/', index, name='home'),
    # If you have a home view
]