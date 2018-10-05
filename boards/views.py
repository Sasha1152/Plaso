from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . models import Board


def home(request):
    boards = Board.objects.all()
    # boards_names = list()
    # for board in boards:
    #     boards_names.append(board.name)
    #
    # response_html = '<br>'.join(boards_names)

    # return HttpResponse("Home page")
    # return HttpResponse(response_html)
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {board:'board'})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})
