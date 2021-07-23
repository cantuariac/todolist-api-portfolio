from django.db.models import fields
from rest_framework import serializers

from django.contrib.auth.models import User, Group

from .models import Tarefa

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'groups', 'url']
        
class TarefaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
        

        entrega = serializers.DateTimeField(format="%Y-%m-%d")