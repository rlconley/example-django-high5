from django.db import models


class HighFive(models.Model):
    title = models.CharField(max_length=150, blank=True)
    text = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
