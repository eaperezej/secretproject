from django.db import models
from django.db.models.aggregates import Sum
from shared.db.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Team(BaseModel):
    name = models.CharField(
        _("Name"),
        max_length=256,
        unique=True
    )

    city = models.CharField(
        _("City"),
        max_length=256
    )

    @property
    def goals_count(self):
        return self.players.aggregate(goals=Sum("goals"))["goals"]

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}={self.name}, City={self.city}"
