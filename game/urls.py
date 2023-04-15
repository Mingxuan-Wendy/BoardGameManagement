from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game_detail'),
    path('categories/', views.CategoriesList.as_view(), name='categories_list'),
]
