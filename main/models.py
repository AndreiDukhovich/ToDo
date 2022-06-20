from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    topic = models.CharField('Topic', max_length=50, primary_key=True)

    def __str__(self):
        return self.topic


class Action(models.Model):
    person = models.CharField('Person', max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=50)
    discription = models.TextField('Discription', blank=True)
    date = models.DateField('Date', blank=True, null=True)
    time = models.TimeField('Time', blank=True, null=True)
    important = models.BooleanField('Important', default=False)
    complete = models.BooleanField('Complete', default=False)

    def __str__(self):
        return f'{self.person}:{self.title}'
