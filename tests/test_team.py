import pytest
from team.models import Team
from django.db.utils import IntegrityError


@pytest.mark.django_db
class TestTeam:
    def test_create_team(self):
        name = "Niupi"
        city = "Nankatsu"

        team = Team(
            name=name,
            city=city
        )

        team.save()

        assert team.pk is not None
        assert team.name == name
        assert team.city == city

    def test_duplicate_team(self):
        with pytest.raises(IntegrityError):
            name = "Niupi"
            city = "Nankatsu"

            team = Team(
                name=name,
                city=city
            )

            team.save()

            duplicate_team = Team(
                name=name,
                city=city
            )

            duplicate_team.save()
