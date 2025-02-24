from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect #добавлено
from .models import Task
import json

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all().values()
        return Response({'tasks': list(tasks)})

    def post(self, request):
     
        title = request.data.get('title') or request.POST.get('title')
        description = request.data.get('description') or request.POST.get('description', '')
        if not title:
            return Response({'error': 'Title is required'}, status=status.HTTP_400_BAD_REQUEST)
        task = Task.objects.create(title=title, description=description)
        return redirect('index')  

class TaskDelete(APIView):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('index')  


def index(request):
    tasks = Task.objects.all()  
    total_tasks = tasks.count() 
    completed_tasks = tasks.filter(completed=True).count() 

    
    if total_tasks > 0:
        productivity_percentage = (completed_tasks / total_tasks) * 100
    else:
        productivity_percentage = 0  

    return render(request, 'myapp/index.html', {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'productivity_percentage': round(productivity_percentage, 2), 
    })


class TaskComplete(APIView):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed  
        task.save()
        return redirect('index')  
    
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'PATCH':
        try:
            task = Task.objects.get(id=task_id)
            data = json.loads(request.body)
            task.is_notified = data.get('is_notified', task.is_notified)
            task.save()
            return JsonResponse({'status': 'success', 'task_id': task_id})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

from datetime import datetime
from django.utils import timezone
from datetime import datetime
from django.shortcuts import redirect
from .models import Task

from datetime import datetime
from django.shortcuts import redirect
from .models import Task




from datetime import datetime
from django.shortcuts import redirect
from .models import Task




#defindex(request):
   #return render(request, 'myapp/index.html')  # Укажите путь к шаблону












'''
# Представление для работы с задачами
@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
    def get(self, request):
        tasks = list(Task.objects.values())
        return JsonResponse({'tasks': tasks}, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        task = Task.objects.create(title=data['title'], description=data.get('description', ''))
        return JsonResponse({'id': task.id, 'title': task.title, 'description': task.description})

@method_decorator(csrf_exempt, name='dispatch')
class TaskDeleteView(View):
    def delete(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return JsonResponse({'message': 'Task deleted successfully'})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)

from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')  # Указываем путь к шаблону






from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
import json

from .serializers import HeroSerializer
from .models import Hero

# Существующий HeroViewSet
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
# myapp/views.py









from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Task
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Task

from django.http import JsonResponse








        
'''    