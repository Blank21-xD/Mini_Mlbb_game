from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    base_hp = models.IntegerField(default=2500)
    base_attack = models.IntegerField(default=115)

    def __str__(self):
        return f"{self.name} ({self.role})"
