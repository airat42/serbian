from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})

# class Home(ListWiew):
#     model = Dictionary
#     template_name = 'main/index.html'
    
