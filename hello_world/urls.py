from django.urls import path
from hello_world.views import helloWorld

urlpatterns = [
    path('h', helloWorld),
]