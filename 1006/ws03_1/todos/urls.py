from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name="index"),
    path('todos/create/', views.create, name="create"),
]
