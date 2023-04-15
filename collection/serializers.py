from rest_framework import serializers
from .models import Collection, Game_Wishlist, Game_Blacklist
from game.models import Game


class Game_WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Wishlist
        fields = '__all__'

class Game_BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Blacklist
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())

    class Meta:
        model = Collection
        fields = '__all__'