from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

class ReactorModel(models.Model):

    CONDITION_CHOICES = (
        ('EFV', 'Exact field value'),
        ('RE', 'Regex'),
    )

    name = models.CharField(max_length=255)
    conditions = JSONField()

    def __str__(self):
        return self.name