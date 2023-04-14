from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='username')
    tele_id = models.CharField('Telegram ID', max_length=50)

    def __str__(self):
        return str(self.user)

