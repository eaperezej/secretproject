from django.db import models
from team.models import Team
from shared.db.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Player(BaseModel):
    name = models.CharField(
        _("Name"),
        max_length=256
    )

    goals = models.IntegerField(
        _("Goals"),
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="players"
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}={self.name}, Goals={self.goals}>"
