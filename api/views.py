from django.shortcuts import render
from api.serializers import *
from rest_framework import generics
from main.models import Action, Archive, Person, PerTask, Topic
from datetime import datetime
from json import dumps, loads


class TasksAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        date = self.request.query_params.get('date', None)
        if id and date:
            date = datetime.strptime(date, "%d.%m.%Y").date()
            return (Action.objects.select_related('person')
                            .filter(person__id=id)
                            .filter(date=date).order_by('-important'))
        elif id:
            return (Action.objects.select_related('person')
                        .filter(person__id=id).order_by('-important'))
        elif date:
            date = datetime.strptime(date, "%d.%m.%Y").date()
            return (Action.objects.select_related('person')
                            .filter(date_lt=date))
            
class ArchivesAPIView(generics.ListCreateAPIView):
    serializer_class = ArchiveSerializers
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        if id:
            date = self.request.query_params.get('date', None)
            if date:
                date = datetime.strptime(date, "%d.%m.%Y").date()
                return (Archive.objects.select_related('person')
                                .filter(person__id=id)
                                .filter(date=date))
            else:
                return (Archive.objects.select_related('person')
                            .filter(person__id=id))
            
            
class TaskAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializers
    queryset = Action.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        complete = self.request.query_params.get('complete', None)
        create_new_date = self.request.query_params.get('createnewdate', None)
        action_data =  super().get(request, *args, **kwargs)
        if complete:
            self.get_object().complete_task()
        elif create_new_date:
            self.get_object().create_action_for_new_date()
        return action_data
        

class TaskCompleteAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializers
    queryset = Action.objects.all()
    lookup_field = 'id'


class TopicAPIView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializers


class TeleAPIView(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = TeleSerializers
    lookup_field = 'tele_id'

    def get_object(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return  self.queryset.get(user__id=user_id)
        return super().get_object()


class ArchiveAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = ArchiveSerializers
    queryset = Archive.objects.all()
    lookup_field = 'id'


class PerTaskAPIView(generics.ListCreateAPIView):
    serializer_class = PerTaskSerializers
    queryset = PerTask.objects.all()


    def get_queryset(self):
        date = self.request.query_params.get('date')
        time = self.request.query_params.get('time')
        if date and time: 
            return self.queryset.filter(date__lte=date, time__lte=time)
        
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
        

class PerTaskAPIDelete(generics.DestroyAPIView):
    serializer_class = PerTaskSerializers
    queryset = PerTask.objects.all()
    lookup_field = 'id'





