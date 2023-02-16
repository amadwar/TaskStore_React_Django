from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["Name","Rolle"]

class Groupserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields=["name","members"]

class Taskserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields=["id","type","title","description","due_date","create_date","modification_date","assigned_user","assigned_group","created_by","modified_by","status"]

class TaskListserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskList
        fields=["id","type","label","tasks"]

class Boradserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields=["Name","columns"]
