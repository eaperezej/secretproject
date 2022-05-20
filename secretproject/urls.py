from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import TeamViewSet, PlayerViewSet


router = DefaultRouter()
router.register(r"player", PlayerViewSet, basename="player")
router.register(r"team", TeamViewSet, basename="team")

urlpatterns = [
    path("", include(router.urls)),
]
