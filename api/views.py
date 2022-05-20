from rest_framework.viewsets import ModelViewSet
from api.serializers import PlayerSerializer, TeamSerializer
from player.models import Player
from team.models import Team


class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
