from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_word, name='index'),
]