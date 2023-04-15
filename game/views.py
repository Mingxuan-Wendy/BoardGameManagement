from rest_framework import generics
from .models import Game, Categories
from .serializers import GameSerializer, CategoriesSerializer

class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CategoriesList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
