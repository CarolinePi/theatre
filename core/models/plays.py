from django.db import models
from django.urls import reverse


class Play(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()

    performance = models.ForeignKey("Performance", on_delete=models.CASCADE)
    hall = models.ForeignKey("Hall", on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = (("editable", "Can be edited"), )

    def __str__(self):
        return f"{self.performance.title} {self.time}"

    def get_absolute_url(self):
        return reverse('core:play', args=[str(self.id)])


