from django.urls import path

from . import views

app_name = 'eithers'

urlpatterns = [
    path('', views.index, name='index'),
    path('eithers/create/', views.create, name="create"),
    path('eithers/<int:pk>/', views.detail, name="detail"), 
    path('eithers/random/', views.random, name="random"),
    path('eithers/<int:pk>/update/',views.update, name="update"),
    path('eithers/<int:pk>/delete/', views.delete, name="delete"),
    path('eithers/<int:pk>/comment/', views.comment_create, name="comment_create"),
    path('eithers/<int:question_pk>/comment_delete/<int:comment_pk>/', views.comment_delete, name="comment_delete"),   
]
