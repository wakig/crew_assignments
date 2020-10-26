from django.urls import path
from . import views

app_name = 'crew_assignments'
urlpatterns = [
    path('', views.index, name='crew_home'),
]