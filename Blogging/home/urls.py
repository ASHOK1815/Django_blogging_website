from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
     path('contact', views.contact, name='contact'),
     path('about', views.about, name='about'),
     path('', views.home, name='home'),
     path('search', views.search, name='search'),
     path('signup', views.handlesignup, name='signup'),
     path('login', views.Login, name='Login'),
     path('logout', views.Logout, name='Logout'),

]