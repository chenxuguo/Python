# from django.shortcuts import render
from django.http import HttpResponse, Http404
from boards.models import Board
from django.shortcuts import render, get_object_or_404


# Create your views here.


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
#    try:
#        board = Board.objects.get(pk=pk)
#    except Board.DoesNotExist:
#        raise Http404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
