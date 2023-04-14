from django.urls import path
from . import views 

urlpatterns = [
    path('tasks/', views.TasksAPIView.as_view()),
    path('task/<int:id>', views.TaskAPIView.as_view()),
    path('tele_user/', views.TeleAPIView.as_view()),
    path('tele_user/<int:tele_id>', views.TeleAPIView.as_view()),
    path('topic/', views.TopicAPIView.as_view()),  
    path('complete_task/<int:id>', views.TaskCompleteAPIView.as_view()), 
    path('archive/<int:id>', views.ArchiveAPIView.as_view()),
    path('archives/', views.ArchivesAPIView.as_view()),
    path('pertasks/', views.PerTaskAPIView.as_view()),
    path('del_pertask/<int:id>', views.PerTaskAPIDelete.as_view()),
    
]