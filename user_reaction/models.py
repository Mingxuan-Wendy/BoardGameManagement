from django.db import models
from django.contrib.auth.models import User

class UserReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.IntegerField()
    REACTION_TYPE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike')
    ]
    reaction_type = models.CharField(max_length=10, choices=REACTION_TYPE_CHOICES)

    class Meta:
        unique_together = ('user', 'game_id')
