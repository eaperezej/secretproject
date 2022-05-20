from rest_framework import serializers
from player.models import Player
from team.models import Team


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "name", "goals", "team"]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "city", "players", "goals_count"]
        extra_kwargs = {
            "players": {"read_only": True},
            "goals_count": {"read_only": True}
        }
