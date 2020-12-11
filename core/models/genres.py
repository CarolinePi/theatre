from django.db import models


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
