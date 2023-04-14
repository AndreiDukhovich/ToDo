from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/', include('api.urls')),
    path('accounts/', include('profileapp.urls')),
]
'''
path('__debug__/', include('debug_toolbar.urls')),'''