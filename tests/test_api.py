import pytest
import json
from rest_framework.test import APIClient
from team.models import Team
from player.models import Player


@pytest.fixture()
def api_client():
    return APIClient


@pytest.fixture()
def team_niupi():
    name = "Niupi"
    city = "Nankatsu"

    team = Team(
        name=name,
        city=city
    )
    team.save()

    return team


@pytest.fixture()
def oliver_atom(team_niupi):
    name = "Oliver"
    goals = 10

    player = Player(
        name=name,
        goals=goals,
        team=team_niupi
    )
    player.save()

    return player


@pytest.mark.django_db
class TestTeamApi:
    team_endpoint = "/team/"

    def test_get_response_team_service(self, api_client):
        response = api_client().get(self.team_endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0

    def test_list_team(self, api_client, team_niupi):
        response = api_client().get(self.team_endpoint)
        team = json.loads(response.content)

        assert response.status_code == 200
        assert len(team) == 1
        assert team[0]["name"] == team_niupi.name

    def test_list_team_by_id(self, api_client, team_niupi):
        url = self.team_endpoint + str(team_niupi.pk) + "/"
        response = api_client().get(url)

        team = json.loads(response.content)

        assert response.status_code == 200
        assert team["id"] == team_niupi.pk

    def test_create_team(self, api_client):
        expected = {
            "name": "Niupy",
            "city": "Nankatsu"
        }

        response = api_client().post(
            self.team_endpoint,
            data=expected,
            format="json"
        )

        team = json.loads(response.content)

        assert response.status_code == 201
        assert team["name"] == expected["name"]
        assert team["city"] == expected["city"]

    def test_update_team(self, api_client, team_niupi):
        url = self.team_endpoint + str(team_niupi.pk) + "/"

        expected = {
            "name": "Fake_Niupy"
        }

        response = api_client().patch(
            url,
            data=expected,
            format="json"
        )

        team = json.loads(response.content)

        assert response.status_code == 200
        assert team["name"] == expected["name"]
        assert team["city"] == team_niupi.city

    def test_remove_team(self, api_client, team_niupi):
        url = self.team_endpoint + str(team_niupi.pk) + "/"

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Team.objects.count() == 0

    def test_team_goals_count(self, api_client, team_niupi):
        oliver = Player.objects.create(
            name="Oliver Atom",
            goals=10,
            team=team_niupi
        )

        andy = Player.objects.create(
            name="Andy Johnson",
            goals=3,
            team=team_niupi
        )

        url = self.team_endpoint + str(team_niupi.pk) + "/"
        response = api_client().get(url)
        team = json.loads(response.content)

        assert response.status_code == 200
        assert len(team["players"]) == 2
        assert team["goals_count"] == oliver.goals + andy.goals


@pytest.mark.django_db
class TestPlayerApi:
    player_endpoint = "/player/"

    def test_get_response_player_service(self, api_client):
        response = api_client().get(self.player_endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 0

    def test_list_player(self, api_client, oliver_atom):
        response = api_client().get(self.player_endpoint)
        players = json.loads(response.content)

        assert response.status_code == 200
        assert len(players) == 1
        assert players[0]["name"] == oliver_atom.name

    def test_list_player_by_id(self, api_client, oliver_atom):
        url = self.player_endpoint + str(oliver_atom.pk) + "/"
        response = api_client().get(url)

        player = json.loads(response.content)

        assert response.status_code == 200
        assert player["id"] == oliver_atom.pk

    def test_create_player(self, api_client, team_niupi):
        expected = {
            "name": "Oliver Atom",
            "team": team_niupi.pk,
            "goals": 10
        }

        response = api_client().post(
            self.player_endpoint,
            data=expected,
            format="json"
        )

        player = json.loads(response.content)

        assert response.status_code == 201
        assert player["name"] == expected["name"]
        assert player["goals"] == expected["goals"]
        assert player["team"] == team_niupi.pk

    def test_update_player(self, api_client, oliver_atom):
        url = self.player_endpoint + str(oliver_atom.pk) + "/"

        expected = {
            "name": "Andy Johnson"
        }

        response = api_client().patch(
            url,
            data=expected,
            format="json"
        )

        team = json.loads(response.content)

        assert response.status_code == 200
        assert team["name"] == expected["name"]
        assert team["goals"] == oliver_atom.goals

    def test_remove_player(self, api_client, oliver_atom):
        url = self.player_endpoint + str(oliver_atom.pk) + "/"

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Player.objects.count() == 0
