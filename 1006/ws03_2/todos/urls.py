from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name="index"),
    path('todos/create/', views.create, name="create"),
    path('todos/<int:pk>/', views.change, name="change"),
    path('todos/<int:pk>/delete/',views.delete, name="delete"),
]
