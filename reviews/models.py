from django.db import models
from custom_user.models import CustomUser
from game.models import Game

class GameReviewRating(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('custom_user', 'game')
