from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'work'),
        ('personal','pesonal'),
        ('urgent','urgent'),
        ('other','other'),
    ]

    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,default='work')

    def __str__(self):
        return self.title

