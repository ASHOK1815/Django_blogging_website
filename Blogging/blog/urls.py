from django.contrib import admin
from django.urls import path
from blog import views 

urlpatterns = [
    
     path('<str:slug>', views.blogpost, name='blogpost'),
     path('', views.bloghome, name='bloghome')
]
