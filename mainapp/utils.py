from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # Creation TimeStamp Caputre
    updated_at = models.DateTimeField(auto_now=True) # Last Update TimeStamp Caputre

    class Meta:
        abstract = True