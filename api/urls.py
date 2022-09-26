from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from . import views

app = "api"

urlpatterns = [
    path('', views.api, name='api'),
]
