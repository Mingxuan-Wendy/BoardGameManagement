from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.CollectionListCreate.as_view(), name='collection_list_create'),
    path('collections/<int:pk>/', views.CollectionRetrieveUpdateDestroy.as_view(), name='collection_retrieve_update_destroy'),
    path('wishlist/', views.Game_WishlistListCreate.as_view(), name='game_wishlist_list_create'),
    path('wishlist/<int:pk>/', views.Game_WishlistRetrieveUpdateDestroy.as_view(), name='game_wishlist_retrieve_update_destroy'),
    path('blacklist/', views.Game_BlacklistListCreate.as_view(), name='game_blacklist_list_create'),
    path('blacklist/<int:pk>/', views.Game_BlacklistRetrieveUpdateDestroy.as_view(), name='game_blacklist_retrieve_update_destroy'),
    path('user/<int:user_id>/games/', views.UserGameListView.as_view(), name='user-game-list'),
]
