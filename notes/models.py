from django.db import models


class Notes(models.Model):
    note_title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
