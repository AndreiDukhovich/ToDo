from django.urls import path, include
from django.views import View
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add_action', views.add_action, name='add_action'),
    path('xui', views.hui, name='xui'),
    path('task/today', views.today, name='today'),
    path('task/tomorrow', views.tomorrow, name='tomorrow'),
    path('task/important', views.important, name='important'),
    path('task/list', views.tasks_list, name='tasks_list'),
    path('task/<str:title>', views.info_task, name='info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/registration', views.registration, name='registration'),
    
]
