from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'To Do'
        verbose_name_plural = 'To Do List'