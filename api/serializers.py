from main.models import Action, Archive, PerTask, Person, Topic
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class ArchiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = '__all__'

class TopicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TeleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PerTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = PerTask
        fields = '__all__'