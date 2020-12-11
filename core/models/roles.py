from django.db import models
from django.db.models import Q


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)

    performance = models.ForeignKey("Performance", on_delete=models.CASCADE)
    actor = models.ForeignKey(
        "Worker",
        on_delete=models.SET_NULL,
        limit_choices_to=Q(position__title="Actor"),
        null=True
    )

    def __str__(self):
        return f"{self.title} in {self.performance.title}"
