from django.db import models
from django.db.models.aggregates import Max


class GameType(models.Model):
    label = models.CharField(max_length=50)