from django.db import models
from django.urls import reverse

# TODO: убрать position?


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    ipn = models.UUIDField(max_length=15)
    salary = models.IntegerField(default=10000)

    biography = models.TextField(null=True)
    
    position = models.ForeignKey("Position", on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = (("editable", "Can be edited"), )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        if self.position.title == 'Actor':
            return reverse('core:actor', args=[str(self.id)])

        if self.position.title == 'Director':
            return reverse('core:director', args=[str(self.id)])

    def get_image_url(self):
        return f'images/workers/{self.last_name}_{self.first_name}.jpg'

