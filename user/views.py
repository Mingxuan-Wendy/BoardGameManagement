from rest_framework import generics
from .models import CustomUser, Friends, User_Settings, System_Settings
from .serializers import CustomUserSerializer, FriendsSerializer, User_SettingsSerializer, System_SettingsSerializer

class CustomUserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class FriendsListCreate(generics.ListCreateAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

class FriendsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friends
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

class User_SettingsListCreate(generics.ListCreateAPIView):
    queryset = User_Settings.objects.all()
    serializer_class = User_SettingsSerializer

class User_SettingsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_Settings.objects.all()
    serializer_class = User_SettingsSerializer

class System_SettingsListCreate(generics.ListCreateAPIView):
    queryset = System_Settings.objects.all()
    serializer_class = System_SettingsSerializer

class System_SettingsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = System_Settings.objects.all()
    serializer_class = System_SettingsSerializer
