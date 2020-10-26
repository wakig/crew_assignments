from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from passenger_view.models import *


def index(request):
    return HttpResponse("Hello, world. You're at the crew assignments index.")
    
class HomeView(View):
    template_name = 'crew_assignments/home_view.html'
    
    def get(self, request, *args, **kwargs):
        context = {:}