# from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Board
from django.shortcuts import render

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})
