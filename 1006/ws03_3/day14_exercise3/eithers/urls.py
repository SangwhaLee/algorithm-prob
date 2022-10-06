from django.urls import path

from . import views

app_name = 'eithers'

urlpatterns = [
    path('', views.index, name='index'),
    path('eithers/create/', views.create, name="create"),
    path('eithers/<int:pk>/', views.detail, name="detail"), 
    path('eithers/random/', views.random, name="random"),
    path('eithers/<int:pk>/comment', views.comment_create, name="comment_create"),   
]
