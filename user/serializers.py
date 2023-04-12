from rest_framework import serializers
from .models import CustomUser, Friends, User_Settings, System_Settings

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'

class User_SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Settings
        fields = '__all__'

class System_SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_Settings
        fields = '__all__'
