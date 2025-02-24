from django.urls import path
from . import views

app_name ='cars'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('api/view_car/<int:id>', views.fetch_car, name='view'),
    path('delete/', views.delete, name='delete'),
]
