from django.db import models


class Event(models.Model):
    title = models.CharField("제목", max_length=200)
    description = models.TextField(null=True, blank=True)
    budget = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
