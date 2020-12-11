from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    seat = models.IntegerField()
    sector = models.CharField(max_length=15)

    play = models.ForeignKey("Play", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Ticket {self.customer.last_name}"
