from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet, TarefaViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'tarefas', TarefaViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('', include(router.urls)),
]
