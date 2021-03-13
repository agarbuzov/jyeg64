from django.db import models


class Data(models.Model):
    name = models.JSONField()

    def __str__(self):
        return self.name
