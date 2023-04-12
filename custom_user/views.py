from rest_framework import generics
from .models import CustomUser, Friends, User_Settings, System_Settings
from .serializers import CustomUserSerializer, FriendsSerializer, User_SettingsSerializer, System_SettingsSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

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

class Register(APIView):
    def post(self, request):
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        user = authenticate(
            request,
            username=request.data.get("username"),
            password=request.data.get("password")
        )
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
