from django.urls import path
from Taskapp.api.v1 import views

app_name = 'task'
urlpatterns = [
    path('test/', views.Test, name='test'),
    path('create/', views.Create_Product, name='create'),
    path('view/', views.View_Product, name='view'),
]