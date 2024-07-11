# myapp/views.py

from django.shortcuts import render

def home(request):
    return render(request,'myapp/home.html')
def connect_four(request):
    return render(request, 'myapp/connect_four.html')
def wordle(request):
    return render(request,'myapp/word.html')
def flappybird(request):
    return render(request,'myapp/flappybird.html')
def index(request):
    return render(request,'myapp/index.html')