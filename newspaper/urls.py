from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
]
app_name = "newspaper"
