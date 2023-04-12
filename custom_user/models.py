from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128)
    salt = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=30, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_users')
    last_update_time = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_users')
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

class Friends(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='custom_user')
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
