from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserListCreate.as_view(), name='customuser_list_create'),
    path('users/<int:pk>/', views.CustomUserRetrieveUpdateDestroy.as_view(), name='customuser_retrieve_update_destroy'),
    path('friends/', views.FriendsListCreate.as_view(), name='friends_list_create'),
    path('friends/<int:pk>/', views.FriendsRetrieveUpdateDestroy.as_view(), name='friends_retrieve_update_destroy'),
    path('user_settings/', views.User_SettingsListCreate.as_view(), name='user_settings_list_create'),
    path('user_settings/<int:pk>/', views.User_SettingsRetrieveUpdateDestroy.as_view(), name='user_settings_retrieve_update_destroy'),
    path('system_settings/', views.System_SettingsListCreate.as_view(), name='system_settings_list_create'),
    path('system_settings/<int:pk>/', views.System_SettingsRetrieveUpdateDestroy.as_view(), name='system_settings_retrieve_update_destroy'),
]
