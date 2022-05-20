from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateField(
        _("Created at"),
        auto_now_add=True,
        null=True
    )

    updated_at = models.DateField(
        _("Updated at"),
        auto_now=True
    )

    class Meta:
        abstract = True
