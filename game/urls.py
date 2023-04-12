from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GameList.as_view(), name='game_list'),
    path('categories/', views.CategoriesList.as_view(), name='categories_list'),
]
