from django.db import models
from django.db.models import Q


# TODO: добавить описание и цитату из пъесы!!!
from django.urls import reverse


class Performance(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    year = models.DateField()
    description = models.TextField(null=True)

    director = models.ForeignKey("Worker",
                                 on_delete=models.SET_NULL,
                                 limit_choices_to=Q(position__title="Director"),
                                 null=True)
    genre = models.ForeignKey("Genre", on_delete=models.SET_NULL, null=True)
    orchestra = models.ForeignKey("Orchestra", on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = (("editable", "Can be edited"), )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:performance', args=[str(self.id)])

    def get_image_url(self):
        return f'images/performances/{self.title}.jpg'
