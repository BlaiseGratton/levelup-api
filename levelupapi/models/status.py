from django.db import models


class Status(models.Model):
    label = models.CharField(max_length=50)