from django.db import models
from django.urls import reverse


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=100, null=True)
    text = models.TextField(max_length=1000, null=True)

    class Meta:
        permissions = (("editable", "Can be edited"), )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('core:author', args=[str(self.id)])

    def get_image_url(self):
        return f'images/authors/{self.last_name}_{self.first_name}.jpg'
