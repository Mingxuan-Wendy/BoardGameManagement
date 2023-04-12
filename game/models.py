from django.db import models

class Game(models.Model):
    rank = models.IntegerField()
    bgg_url = models.URLField()
    game_id = models.IntegerField()
    names = models.CharField(max_length=255)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    avg_time = models.IntegerField()
    min_time = models.IntegerField()
    max_time = models.IntegerField()
    year = models.IntegerField()
    avg_rating = models.FloatField()
    geek_rating = models.FloatField()
    num_votes = models.IntegerField()
    image_url = models.URLField()
    age = models.IntegerField()
    mechanic = models.CharField(max_length=255)
    owned = models.IntegerField()
    category = models.CharField(max_length=255)
    designer = models.CharField(max_length=255)
    weight = models.FloatField()

class Categories(models.Model):
    category_name = models.CharField(max_length=255)

class Game_Category_Relation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
