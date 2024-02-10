from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('exchanges/<int:exchange_name>/', views.exchanges),
]


