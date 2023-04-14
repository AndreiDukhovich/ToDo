from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.registration, name='registration'),
    path('registration/<int:id>', views.registration, name='registration'),
    path('telegram/<int:id>', views.telgramconferm, name='telgramconferm'),
    path('settings/', views.profile_settings, name='profile'),
    path('loginid/<int:id>', views.login_with_tele_id, name='loginid'),
    
]
