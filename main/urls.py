from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add_action', views.add_action, name='add_action'),
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('task/<str:date>/', views.tasks_list, name='task_list_with_date'),
    path('tasks/<str:filter_param>/', views.tasks_list, name='task_list_with_param'),
    path('edit/<int:loc>/<int:id>', views.edit, name='edit'),
    path('archive/<int:id>', views.info_archive_task, name='archiveinfo'),
    path('task/<int:id>', views.info_task, name='info'),
    path('datetasks', views.task_for_date, name='taks_for_date'),
]
