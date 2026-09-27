from django.db import models


class Hero(models.Model):

    name = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=50)
    base_attack = models.IntegerField(default=100)
    base_hp = models.IntegerField(default=1000)


def __str__(self):
    return f"{self.name} ({self.role})"
