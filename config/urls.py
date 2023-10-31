
from django.contrib import admin
from django.urls import path

from app.views import hello_view

urlpatterns = [
    path("<name>/", hello_view),
]
