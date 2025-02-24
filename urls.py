'''
from django.urls import path
from .views import TaskList
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Главная страница с фронтендом
    path('tasks/', TaskList.as_view(), name='task-list'),
  
]



n2(work)
from django.urls import path
from .views import TaskList, TaskDelete, index

urlpatterns = [
    path('', index, name='index'),  # Главная страница с фронтендом
    path('tasks/', TaskList.as_view(), name='task-list'),  # API для задач
    path('tasks/<int:task_id>/delete/', TaskDelete.as_view(), name='task-delete'),  # Удаление задачи
]

'''
from django.urls import path
from .views import TaskList, TaskDelete, TaskComplete, index
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

  

urlpatterns = [
    path('', index, name='index'),  
    path('tasks/', TaskList.as_view(), name='task-list'),  
    path('tasks/<int:task_id>/delete/', TaskDelete.as_view(), name='task-delete'), 
    path('tasks/<int:task_id>/complete/', TaskComplete.as_view(), name='task-complete'), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Эндпоинт для получения токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Эндпоинт для обновления токена
    path('tasks/<int:task_id>/', views.update_task, name='task-update'),
    
    
    
]










