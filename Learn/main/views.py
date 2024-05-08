from django.shortcuts import render
from .models import Film

def films_list(request):
    # Получаем список всех фильмов из базы данных
    films = Film.objects.all()


    return render(request, 'index.html', {'films': films})

