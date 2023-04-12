from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.GameReviewRatingList.as_view(), name='review_rating_list'),
    path('reviews/<int:pk>/', views.GameReviewRatingDetail.as_view(), name='review_rating_detail'),
]
