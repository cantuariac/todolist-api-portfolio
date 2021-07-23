from todo_api.models import *
from faker import Faker
from django.contrib.auth.models import User
import random

faker: Faker = Faker(locale='pt-br')

user = User.objects.create_user('admin', password='1q2w')
user.is_superuser = True
user.is_staff = True
user.save()

User.objects.create_user('caio', password='1234').save()


for i in range(5):
    nome = faker.first_name()
    username = nome.replace(" ", '')+str(random.randint(0, 100)).lower()

    user = User.objects.create_user(username=username, first_name=nome, password='1234')
    user.save()


users = list(User.objects.all().exclude(username='admin'))

for i in range(30):
    Tarefa(usuario=users[random.randint(0, len(users)-1)], descricao=faker.catch_phrase(),
           nome=faker.catch_phrase(), entrega=faker.future_datetime('-30d')).save()
