from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    salt = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_users')
    last_update_time = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_users')
    email = models.EmailField(unique=True)

class Friends(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friend')
    added_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('blocked', 'Blocked')
    )
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='active')

class User_Settings(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    notification_preferences = models.JSONField(default=dict)
    privacy_settings = models.JSONField(default=dict)

class System_Settings(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    password_settings = models.JSONField(default=dict)
    email_settings = models.JSONField(default=dict)
