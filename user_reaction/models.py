from django.db import models
from custom_user.models import CustomUser

class UserReaction(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game_id = models.IntegerField()
    REACTION_TYPE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike')
    ]
    reaction_type = models.CharField(max_length=10, choices=REACTION_TYPE_CHOICES)

    class Meta:
        unique_together = ('custom_user', 'game_id')
