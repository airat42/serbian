from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from main.models import Dictionary
import random

rand_int = random.randint(0, len(Dictionary.objects.all()))
queryset1 = Dictionary.objects.raw(f'SELECT * FROM main_dictionary WHERE id = {rand_int}')

class Home(ListView):
    model = Dictionary
    template_name = 'main/index.html'

    def get_queryset(self):
        queryset = list(Dictionary.objects.all().values('russian', 'serbian'))[0]
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queryset1'] = queryset1
        return context
    
