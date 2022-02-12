from django.urls import path
from .views import *
from followapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('followers_count', views.followers_count, name='followers_count'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
