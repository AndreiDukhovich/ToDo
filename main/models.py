from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from profileapp.models import Person
from datetime import datetime as dt, time as timeClass, date as dateClass, timedelta
from profileapp.models import Person
from json import dumps

class Topic(models.Model):
    topic = models.CharField('Topic', max_length=50, primary_key=True)

    def __str__(self):
        return self.topic


class Action(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, db_column='username')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=50)
    discription = models.TextField('Discription', blank=True)
    date = models.DateField('Date', blank=True, null=True)
    time = models.TimeField('Time', blank=True, null=True)
    important = models.BooleanField('Important', default=False)
    period = models.CharField(max_length=10, null=True, blank=True)

    def create_action_for_new_date(self):
        date = dt.now().date() + timedelta(days=1)
        new_date = get_next_valid_date(date=date, period=self.period)
        Action.objects.get_or_create(person=self.person, topic=self.topic, title=self.title,
            discription=self.discription, date=new_date, time=self.time,
            important=self.important, period=self.period)
        PerTask.objects.filter(name=self.id).delete()
 
    def __str__(self):
        return f'{self.person}:{self.title} {self.id}'
    
    
    def create_archive_task(self):
        Archive(person=self.person, 
                topic=self.topic, 
                discription=self.discription,
                title=self.title).save()
        
    def complete_task(self):
        self.create_archive_task()
        self.delete()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)            
        try:
            tele_id = Person.objects.get(user=self.person).tele_id
            if self.date and self.time and not self.period:
                create_task_by_date_and_time(task_id=self.id, date=self.date,
                                            time=self.time, tele_id=tele_id)
            elif self.period:
                create_periodic_task_by_time(time=self.time, date=self.date, tele_id=tele_id, 
                                            task_id=self.id, period=self.period)
        except Person.DoesNotExist:
            pass

    def delete(self, *args, **kwargs):
        PerTask.objects.filter(name=self.id).delete()
        return super().delete(*args, **kwargs)
    
    class Meta:
        unique_together = ['person', 'title', 'date']
    


class Archive(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, 
                            db_column='username')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=50)
    discription = models.TextField('Discription', blank=True)
    date = models.DateField('Date', auto_now=True)
    time = models.TimeField('Time', auto_now=True)

    def __str__(self):
        return f'{self.person}:{self.title} {self.id}'



def create_task_by_date_and_time(task_id: int, date:dateClass, time:timeClass, tele_id:int):
    PerTask(name=task_id,
            date=date,
            time=time,
            action='datetime_telegram_alert',
            kwargs=dumps({"task_id": f"{task_id}", 
                        "user": f'{tele_id}'}),
            period = None
            ).save()


def create_periodic_task_by_time(time: timeClass, date: dateClass, tele_id: int, task_id: int, 
                                period: str):
    '''Create periodic sending task which is running depending on parameter 
        today or tomorow and given time.'''
    PerTask(name=task_id,
            date = date,
            time=time,
            action='telegram_alert_with_periodicity',
            kwargs=dumps({"task_id": f'{task_id}', 
                        "user": f'{tele_id}',
                        'period': f'{period}'}),
            period = period
            ).save()
    

class PerTask(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    action = models.CharField('Name of action', max_length=50)
    kwargs = models.TextField('Json kwargs', blank=True, null=True)
    period = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.name
                

def get_next_valid_date(date: dateClass, period: str):
    weekday_and_per_ratio = {
            'ever': range(7),
            'wd': range(5),
            'we': [5, 6]
        }
    for i in range(1, 7):
        if date.weekday() in weekday_and_per_ratio[period]:
            return date
        date += timedelta(days=1)




