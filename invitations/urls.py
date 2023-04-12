from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('invitations', views.InvitationViewSet, basename='invitation')

urlpatterns = router.urls

# urlpatterns = [
#     path('invitations/recommendations/', views.InvitationRecommendationView.as_view(), name='invitation_recommendations'),
# ]
# 用于推荐算法
# 现在，通过GET /api/invitations/recommendations/，您可以访问邀请推荐的功能。
#
# 需要根据实际情况修改InvitationRecommendationView视图以实现您的推荐逻辑。例如，您可以考虑使用协同过滤、基于内容的推荐等技术来实现推荐功能。

