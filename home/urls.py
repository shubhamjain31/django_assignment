from django.urls import path
from . import views

urlpatterns = [
    path('cryptocurrency/', views.cryptocurrency, name='cryptocurrency'),
]