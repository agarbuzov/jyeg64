from django.db import models


class Data(models.Model):
    name = models.JSONField()
