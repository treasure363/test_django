from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('display/<str:name>/', views.display, name='display'),
]
