from django.shortcuts import render
from django.http import HttpResponse


def game_page(request):
    return render(request, 'game/game_page.html')
