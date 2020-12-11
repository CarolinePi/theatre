from django.db import models
from django.db.models import Q


class OrchestraMember(models.Model):
    id = models.AutoField(primary_key=True)
    musician = models.ForeignKey(
        "Worker",
        on_delete=models.CASCADE,
        limit_choices_to=Q(position__title="Musician")
    )
    orchestra = models.ForeignKey("Orchestra", on_delete=models.CASCADE)
