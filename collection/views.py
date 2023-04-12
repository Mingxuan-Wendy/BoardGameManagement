from rest_framework import generics
from .models import Collection, Game_Wishlist, Game_Blacklist
from .serializers import CollectionSerializer, Game_WishlistSerializer, Game_BlacklistSerializer

class CollectionListCreate(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class Game_WishlistListCreate(generics.ListCreateAPIView):
    queryset = Game_Wishlist.objects.all()
    serializer_class = Game_WishlistSerializer

class Game_WishlistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game_Wishlist.objects.all()
    serializer_class = Game_WishlistSerializer

class Game_BlacklistListCreate(generics.ListCreateAPIView):
    queryset = Game_Blacklist.objects.all()
    serializer_class = Game_BlacklistSerializer

class Game_BlacklistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game_Blacklist.objects.all()
    serializer_class = Game_BlacklistSerializer
