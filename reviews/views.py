from rest_framework import generics
from .models import GameReviewRating
from .serializers import GameReviewRatingSerializer

class GameReviewRatingList(generics.ListCreateAPIView):
    queryset = GameReviewRating.objects.all()
    serializer_class = GameReviewRatingSerializer

class GameReviewRatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameReviewRating.objects.all()
    serializer_class = GameReviewRatingSerializer
