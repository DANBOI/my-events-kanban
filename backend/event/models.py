from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name')


class Event(models.Model):
    category = models.ForeignKey(
        Category, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    participation_fee = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='events', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    # def created_at_formatted(self):
    #     return defaultfilters.date(self.created_at, 'M d, Y')
