from rest_framework import viewsets, mixins
from .models import UserReaction
from .serializers import UserReactionSerializer

class UserReactionViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = UserReaction.objects.all()
    serializer_class = UserReactionSerializer
