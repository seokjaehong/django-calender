from django.db import models

from django.urls import reverse


class Event(models.Model):
    title = models.CharField("제목", max_length=200)
    description = models.TextField(null=True, blank=True)
    budget = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
