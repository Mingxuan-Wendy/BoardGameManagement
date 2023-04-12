from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('reactions', views.UserReactionViewSet, basename='user_reaction')

urlpatterns = router.urls
