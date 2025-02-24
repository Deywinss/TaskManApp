from django.db import models
from django.conf import settings

from datetime import datetime
import pytz




class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def str(self):
        return self.name


class Task(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)  # Новое поле для отметки выполнен
    created_at = models.DateTimeField(auto_now_add=True) 
    notification_time = models.DateTimeField(default=datetime(2025, 1, 1, 0, 0, 0))  # Укажите значение по умолчанию
    is_notified = models.BooleanField(default=False)  # Флаг, отправлено ли уведомление
    user_id = models.CharField(max_length=50, default=settings.TELEGRAM_USER_ID)
   
    
    def __str__(self):
        return self.title
