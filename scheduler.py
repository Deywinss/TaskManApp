from django.utils import timezone
from django.utils.timezone import make_aware
from .models import Task
from .telegram_bot import send_notification

def send_scheduled_notifications():
    tasks = Task.objects.filter(notification_time__isnull=False)  # Задачи с установленным временем уведомления
    now = timezone.now()  # Осведомлённое текущее время
    for task in tasks:
        # Приведение наивного времени к осведомлённому (если нужно)
        if task.notification_time.tzinfo is None:
            task.notification_time = make_aware(task.notification_time)
        
        # Сравнение осведомлённых времён
        if task.notification_time <= now:
            # Отправляем уведомление
            send_notification(chat_id=946053796, message=f"Напоминание: {task.title}")
            # Убираем время уведомления, чтобы не отправлять повторно
            task.notification_time = None
            task.save()