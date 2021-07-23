from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import generics, viewsets, permissions, views
from rest_framework.response import Response

from .models import Tarefa
from .serializers import TarefaSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class TarefaViewSet(viewsets.ModelViewSet):
    model = Tarefa
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return Tarefa.objects.all()
        else:
            return Tarefa.objects.all().filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

