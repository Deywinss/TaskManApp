from rest_framework import serializers

from .models import Hero
from .models import Task

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')
        
        

from rest_framework import serializers
from .models import Task
from django.conf import settings

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        # Если Telegram ID не указан, добавляем его из настроек
        if 'user_id' not in validated_data:
            validated_data['user_id'] = settings.TELEGRAM_USER_ID
        return super().create(validated_data)