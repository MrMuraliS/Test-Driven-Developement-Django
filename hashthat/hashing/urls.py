from django.urls import path
from . import views

app_name = 'hashing'

urlpatterns = [
    path('', views.home, name='home')
]
