from django.urls import path
from . import views

urlpatterns = [
    path('simple/', views.simple_view, name='simple_view'),
    path('variable/', views.variable_view, name='simple_view'),
    # path('testing', views.testing, name='testing'),  # Add this line to test the function in views.py
]