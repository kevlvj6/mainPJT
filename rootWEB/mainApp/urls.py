from django.contrib import admin
from django.urls import path, include
from mainApp     import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path("", views.login),
    path("main/", views.main),
    path("QNA/" , views.QNA),
]