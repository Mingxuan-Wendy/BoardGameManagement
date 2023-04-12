from django.db import models
from django.contrib.auth.models import User

class Invitation(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invitations')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_invitations')
    game_id = models.IntegerField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    sent_date = models.DateTimeField(auto_now_add=True)
    response_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('sender', 'receiver', 'game_id')
