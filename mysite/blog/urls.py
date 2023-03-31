from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', include)'blog.urls'))
]