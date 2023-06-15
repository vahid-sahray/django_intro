from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=11)
    body = models.TextField()
    created = models.DateTimeField()