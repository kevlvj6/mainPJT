from django.contrib import admin
from django.urls import path, include
from mainApp import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path("", views.info, name="index"),
    path("index", views.index, name="login"),
    path("joinForm/", views.joinForm),
    path("join/", views.join),
    path("login/", views.login),
    path("logout/", views.logout),
    path("main/", views.main),
    path("CCTV/", views.CCTV),
    path("QNA/", views.QNA),
    path("detectme/", views.detectme),
    path("chart/", views.chart),
]
