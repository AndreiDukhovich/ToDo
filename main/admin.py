from django.contrib import admin
from .models import Action, Topic, Archive, PerTask
# Register your models here.
admin.site.register(Action)
admin.site.register(Topic)
admin.site.register(Archive)
admin.site.register(PerTask)