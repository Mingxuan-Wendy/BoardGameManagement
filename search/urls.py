# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_game, name='search_game'),
]
