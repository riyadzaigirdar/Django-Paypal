from django.urls import path, include
from donation import views

urlpatterns = [
    path('', views.index, name='index')
]
