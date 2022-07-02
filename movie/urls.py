from tokenize import Token
from django.urls import path
from .views import CreateLists, DeleteLists, Lists, Redis, UpdateLists

urlpatterns = [
    path('lists', Lists.as_view()),
    path('create_lists', CreateLists.as_view()),
    path('update_lists', UpdateLists.as_view(), name='update-list'),
    path('delete_lists', DeleteLists.as_view(), name='delete-list'),

    path('tes_redis', Redis.as_view()),
]
