from django.urls import path

from . import views

urlpatterns =[
    path("", views.home, name="home"),
    path("login/", views.loginView, name="login"),
    path('index/', views.index, name="index"),
]