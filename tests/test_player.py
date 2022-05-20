import pytest
from player.models import Player
from team.models import Team


@pytest.fixture()
def dummy_team():
    team = Team(
        name="Niupi",
        city="Nankatsu"
    )

    team.save()

    return team


@pytest.mark.django_db
def test_create_player(dummy_team):
    name = "Oliver Atom"
    goals = 10

    player = Player(
        name=name,
        goals=goals,
        team=dummy_team
    )

    player.save()

    assert player.pk is not None
    assert player.team.name == dummy_team.name
    assert player.name == name
    assert player.goals == goals
